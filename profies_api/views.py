from sys import api_version
from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    def get(self, request, format=None):
        api_view=[
            'uses http method (get,post,put,delete) ',
            'Is similar to a django view',
            'gives you most control over application logic',
            'mapped manually to URLs'
        ]
        return Response({'messsage':'Hello', 'api_view':api_view })