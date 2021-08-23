from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None) -> Response:
        """Returns a list of APIView"""
        an_apiview = [
            'User HTTP methods as function',
            'Is similar to traditional Django View',
            'Gives most control over application logic',
            'Is mapped manually to URLs'
        ]
        return Response(data={'message': 'Starting', 'an_apiview': an_apiview})

    def post(self, request) -> Response:
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello! {name}'
            return Response({'message': message})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handling updating an object"""
        return Response({'message': 'Put'})

    def patch(self, request, pk=None):
        """Handling patching an object"""
        return Response({'message': 'Patch'})

    def delete(self, request, pk=None):
        """Handling deleting an object"""
        return Response({'message': 'Delete'})
