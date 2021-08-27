from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from profiles_api import serializers, models, permissions


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    @staticmethod
    def get(request, format=None) -> Response:
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

    @staticmethod
    def put(request, pk=None):
        """Handling updating an object"""
        return Response({'message': 'Put'})

    @staticmethod
    def patch(request, pk=None):
        """Handling patching an object"""
        return Response({'message': 'Patch'})

    @staticmethod
    def delete(request, pk=None):
        """Handling deleting an object"""
        return Response({'message': 'Delete'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    @staticmethod
    def list(request):
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
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    """Handle  creating user authetication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (
        permissions.UpdateOwnStatus,
        IsAuthenticated
    )

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)
