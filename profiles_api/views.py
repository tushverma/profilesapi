from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from profiles_api import serializers, models, permissions


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


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        a_viewset = [
            'User Actions list, create, retrieve, update, partial_updatemethods as function',
            'Gives most control over application logic',
            'Automatically maps to URLs using Router'
        ]
        return Response(data={'message': 'Hello ViewSet', 'a_viewset': a_viewset})

    def create(self, request):
        """Create new hello message"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello! {name}'
            return Response({"message": message})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def retrieve(request, pk=None):
        return Response({'http_method': 'GET'})

    @staticmethod
    def update(request, pk=None):
        return Response({'http_method': 'PUT'})

    @staticmethod
    def partial_update(request, pk=None):
        return Response({'http_method': 'PATCH'})

    @staticmethod
    def destroy(request, pk=None):
        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
