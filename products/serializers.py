from rest_framework import serializers

from . models import Category,File,Product


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title','description','avatar']


class FileSerializers(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['title','file']

class ProductSerializers(serializers.ModelSerializer):
    categories = CategorySerializers(many = True)
    
    class Meta:
        model = Product
        fields = ['title','description','avatar','categories']