from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets
from profiles_api.models import UserProfile

from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions
# Create your views here.



class HelloApiView(APIView):
    """ Test api view """
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """ returns a list of apiview features """
        an_apiview = [
            'uses http methods as function(get,post,put,patch,delete)',
            'is similar to traditional django view',
            'give you the most control over you applicatin login',
            'is mapped manually to url',
        ]

        return Response({'message':"hello!",
                         'an_apiview':an_apiview})
    
    def post(self, request):
        """ create a hello message with our name """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hello {name}"
            return Response({'message':message})
        
        else:
            return Response(
                serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST
                )
      
    def put(self, request, pk=None):
        """ handle updating an object """
        return Response({'method': 'PUT'})
    
    def patch(self, request, pk=None):
        """  handle a partial update of an object """
        return Response({'Method', 'PATCH'})
    
    def delete(self, request, pk=None):
        """ Delete an object """
        return Response({'method': "DELETE"})
    

class HelloViewSet(viewsets.ViewSet):
    """test api view"""
    serializer_class = serializers.HelloSerializer
    def list(self, request):
        """return a hello message"""
        a_viewset = [
            'uses action (list,create,retrieve,update, partial update, destroy)',
            'Automatically maps to urls using routers',
            'provides more functionality with less code',
        ]
        return Response({'message': 'hello',
                         'a_viewset': a_viewset})
    
    def create(self, request):
        """ creatre a new hello message """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"hello {name}"
            return Response({'message': message})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        """ handle getting an object using the pk """
        return Response({'method': 'GET'})
    
    def update(self, request, pk=None):
        """ handle updating an object """
        return Response({'method': 'PUT'})
    
    def partial_update(self, request, pk=None):
        """ handle upadating an field """
        return Response({'method':'PATCH'})
    
    def destroy(sef, request, pk=None):
        return Response({'method':'DELETE'})
    


class UserProfileViewSet(viewsets.ModelViewSet):
    """handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)