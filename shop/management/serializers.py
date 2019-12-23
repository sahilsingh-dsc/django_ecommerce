from rest_framework import serializers
from .models import Category, Product, Slider


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name', 'category_image']

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['product_name', 'product_image']

class SliderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Slider
        fields = ['slider_image']