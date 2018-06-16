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

from .services import HumanService
from .serializers import HumanSerializer, StatsSerializer

class IndexViewSet(GenericViewSet):
    def index(self, request):
        return JsonResponse({'title':'Geonunez Test Meli'})

class HumanViewSet(GenericViewSet):
    """
    Human ViewSet
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

            human = self.humanService.verify(dna)

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
        stats = self.humanService.get_stats()

        serializer = StatsSerializer(stats)

        return Response(serializer.data, status=status.HTTP_200_OK)
