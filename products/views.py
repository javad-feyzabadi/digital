from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . models import Product,Category,File
from . serializers import FileSerializers,ProductSerializers,CategorySerializers


class ProductListView(APIView):

    def get(self,request):
        products = Product.objects.all()
        serializer = ProductSerializers(products, many = True,context = {'request':request})
        return Response(serializer.data)


class ProductDetailView(APIView):

    def get(self,request,pk):
        try:
            product = Product.objects.get(pk = pk)
        except Product.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializers(product,context = {'request':request})
        return Response(serializer.data)

class CategoryListView(APIView):

    def get(self,request):
        categories = Category.objects.all()
        serializer = CategorySerializers(categories, many = True,context = {'request':request})
        return Response(serializer.data)


class CategoryDetailView(APIView):

    def get(self,request,pk):
        try:
            category = Category.objects.get(pk = pk)
        except Category.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)

        serializer = CategorySerializers(category,context = {'request':request})
        return Response(serializer.data)




class FileListView(APIView):

    def get(self,request,product_id):
        files = File.objects.filter(product_id =product_id)
        serializer = FileSerializers(files, many = True,context = {'request':request})
        return Response(serializer.data)


class FileDetailView(APIView):

    def get(self,request,pk,product_id):
        try:
            file = File.objects.get(pk = pk,product_id=product_id)
        except File.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)

        serializer = FileSerializers(file,context = {'request':request})
        return Response(serializer.data)