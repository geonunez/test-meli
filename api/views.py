"""
    Api's views
"""

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .services import MutantService
from .serializers import MutantSerializer

class MutantViewSet(ViewSet):

    def verify(self, request):
        serializer = MutantSerializer(data=request.data)
        if serializer.is_valid():
            adn = serializer.data["adn"]

            if MutantService.is_mutant(adn):
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)

        return Response(status=status.HTTP_400_BAD_REQUEST)
