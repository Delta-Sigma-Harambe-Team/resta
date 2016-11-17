from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
class Products(APIView):
    """
    Observa y pide mas pedidos al almacen
    """
    def get(self, request, format=None): #Proxy to almacen
        r = requests.get('http://localhost:8001/api/v1/products/')
        return Response(r.json())

    def post(self, request, format=None):
        pass