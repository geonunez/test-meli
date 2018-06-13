"""
    Api's views
"""

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

class MutantViewSet(ViewSet):

    def verify(self, request):
        return Response(status=status.HTTP_200_OK)
