# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import status
from .models import Category
from .models import Product
from .serializers import CategorySerializer
from .serializers import ProductSerializer
from .serializers import ProductFlatSerializer
from rest_framework.views import APIView


class ListAllCategory(generics.ListAPIView):
    """
        GET inventory/category/
    """
    queryset = Category.objects.exclude(parent__isnull=True)
    serializer_class = CategorySerializer


class FetchSubCategory(generics.ListAPIView):
    """
        GET inventory/subcategory?id=:id
    """
    queryset = ''

    def get(self, request, *args, **kwargs):
        parent_id = request.GET["id"]
        try:
            queryset = Category.objects.filter(parentCategory_id=parent_id)
            return Response(CategorySerializer(queryset, many=True).data)
        except Category.DoesNotExist:
            return Response(
                data={
                    "message": "Sub Category with parent id: {} does not exist".format(parent_id)
                },
                status=status.HTTP_404_NOT_FOUND
            )


class ProductView(APIView):
    """
        GET inventory/product/?cat=1&subcat4
        POST inventory/product/
    """

    queryset = ''

    def get(self, request):
        parent_id = request.GET.get("cat", '')
        subcat_id = request.GET.get("subcat", '')
        try:
            if parent_id:
                queryset = Product.objects.filter(category=parent_id)
            else:
                if subcat_id:
                    queryset = Product.objects.filter(subCategory=subcat_id)
                else:
                    queryset = Product.objects.all()
            return Response(ProductSerializer(queryset, many=True).data)
        except Product.DoesNotExist:
            return Response(
                data={
                    "message": "No Product Exist"
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def post(self, request):
        product = ProductFlatSerializer(data=request.data)
        if product.is_valid(True):
            product.save()
            return Response(data={'Product Saved'}, status=status.HTTP_201_CREATED)
        else:
            return Response(
                data={
                    "message": "Invalid Product"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

