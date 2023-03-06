from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.



class HelloApiView(APIView):
    """ Test api view """

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