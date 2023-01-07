from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from . models import Product
from . serializers import ProductSerializers


class ProductListView(APIView):

    def get(self,request):
        products = Product.objects.all()
        serializer = ProductSerializers(products, many = True)
        return Response(serializer.data)