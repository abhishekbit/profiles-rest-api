from email import message
from re import I
from sys import api_version
from tkinter import N
from unicodedata import name
from urllib import response
from urllib.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profies_api import serializers


class HelloApiView(APIView):
    """ Test api view"""
    serializer_class = serializers.HelloSerializers 
    def get(self, request, format=None):
        an_api_view = [
            'Uses http method (get,post,put,delete) ',
            'Is similar to a django view',
            'Gives you most control over application logic',
            'Mapped manually to URLs'
        ]
        return Response({'messsage':'Hello', 'api_view':an_api_view })
    
    def post(self, request):
        """ create a hello msg with name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=404)
    
    def put(self, request):
        """ handles update"""
        return Response({'method': 'PUT'})
    
    def delete(self, request):
        """ delete an  object"""
        return Response({'method': 'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """ Test API Viewset """
    serializer_class = serializers.HelloSerializers

    def list(self, request):
        """ returns a hello msg  """
        a_viewset = [
            'Uses actions(list, create, retrieve, update)',
            'Automatically  maps to urls using routers',
            'Provide more functionality with less code'
        ]
        return Response({'message': 'Hello!' , 'a_viewset':a_viewset })
    
    def create(self, request):
        """ creates a new hello msg"""    
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        """ handles getting object with id"""
        return Response({'http_method': ''})
    
    def update(self, request, pk=None):
        """ handles updating object with id"""
        return Response({'http_method': 'PUT'})
    
    def destroy(self, request, pk=None):
        """ handles deleting object with id"""
        return Response({'http_method': 'DELETE'})
