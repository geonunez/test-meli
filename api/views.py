# -*- coding: utf-8 -*-

"""
    Api's views
"""

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import Human
from .services import HumanService
from .serializers import HumanSerializer, StatsSerializer

class IndexViewSet(GenericViewSet):
    def index(self, request):
        return JsonResponse({'title':'Geonunez Test-meli'})

class HumanViewSet(GenericViewSet):
    """
    Human endpoints
    """
    serializer_class = HumanSerializer
    humanService = HumanService()

    def is_mutant(self, request):
        """
        Verifies if a human is or not a mutant, saving the result.
        """
        serializer = HumanSerializer(data=request.data)
        if serializer.is_valid():
            dna = serializer.data["dna"]
            s_dna = ''.join(dna)

            try:
                human = Human.objects.get(dna=s_dna)
            except Human.DoesNotExist:
                is_mutant = self.humanService.is_mutant(dna)
                human = Human.objects.create(dna=s_dna, is_mutant=is_mutant)

            return Response(status= \
                status.HTTP_200_OK if human.is_mutant else status.HTTP_403_FORBIDDEN \
            )

        # I would have preferred to return a HTTP_400_BAD_REQUEST, but the challenge said 403
        return Response(status=status.HTTP_403_FORBIDDEN)

    @method_decorator(cache_page(10))
    def stats(self, request):
        """
        Shows the human stats.
        """
        humans = Human.objects.all()

        total = humans.count()
        count_mutant_dna = count_human_dna = radio = 0

        if total > 0:
            for human in humans:
                count_mutant_dna += 1 if human.is_mutant else 0
            count_human_dna = total - count_mutant_dna
            radio = count_mutant_dna / total

        serializer = StatsSerializer({ \
            'count_mutant_dna': count_mutant_dna, \
            'count_human_dna': count_human_dna, \
            'radio': radio \
        })

        return Response(serializer.data, status=status.HTTP_200_OK)
