from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from decimal import Decimal
from .models import *


class CatagorySerializer(ModelSerializer):
    class Meta:
        model = Catagory
        fields = ["id", "title", "feature_product", "product_count"]
        read_only_fields = ["product_count"]

    feature_product = serializers.StringRelatedField()
    product_count = serializers.IntegerField(read_only=True)


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ["id","title","slug","inventory","price","price_with_tax","description","catagory",]

    price_with_tax = serializers.SerializerMethodField(method_name="calculate_tax")

    def calculate_tax(self, product: Product):
        return product.price * Decimal(1.1)


# __________________________________
# def validate(self, data):
#     if data['password'] != data['confirm_password']:
#         return serializers.ValidationError('Pass word do not match')
#     return data
# ____________________________________
