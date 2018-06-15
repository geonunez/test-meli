# -*- coding: utf-8 -*-

"""
    Api's views
"""

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .models import Human
from .services import HumanService
from .serializers import HumanSerializer, StatsSerializer


class HumanViewSet(ViewSet):
    humanService = HumanService()

    def is_mutant(self, request):
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

    def stats(self, request):
        humans = Human.objects.all()
        total = humans.count()
        mutants = 0
        for human in humans:
            if human.is_mutant:
                mutants += 1
        humans = total - mutants


        data = { \
            'count_mutant_dna': mutants, \
            'count_human_dna': humans, \
            'radio': humans / mutants
        }

        serializer = StatsSerializer(data)

        return Response(serializer.data, status=status.HTTP_200_OK)
