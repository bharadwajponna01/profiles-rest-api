from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
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
    