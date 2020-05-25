from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test APIview"""

    def get(self, request, fomat=None):
        """Return a list of APiview features"""
        an_apiview = [
            'User HTTP methods as function (get, post, patch, put, delete)'
            'Nguyen Thiep Here'
        ]
        return Response({'message': 'Hello', 'an_apiview': an_apiview})
