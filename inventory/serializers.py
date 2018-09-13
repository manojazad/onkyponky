from rest_framework import serializers
from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    subCategory = CategorySerializer()

    class Meta:
        model = Product
        fields = ("id", "name", "category", "subCategory")


class ProductFlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "name", "category", "subCategory")
