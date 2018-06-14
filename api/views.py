# -*- coding: utf-8 -*-

"""
    Api's views
"""

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .services import MutantService
from .serializers import MutantSerializer

class MutantViewSet(ViewSet):
    mutantService = MutantService()

    def is_mutant(self, request):
        serializer = MutantSerializer(data=request.data)
        if serializer.is_valid():
            adn = serializer.data["adn"]

            if self.mutantService.is_mutant(adn):
                return Response(status=status.HTTP_200_OK)

        return Response(status=status.HTTP_403_FORBIDDEN)
