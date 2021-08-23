from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIView"""
        an_apiview = [
            'User HTTP methods as function',
            'Is similar to traditional Django View',
            'Gives most control over application logic',
            'Is mapped manually to URLs'
        ]
        return Response(data={'message': 'Starting', 'an_apiview': an_apiview})
