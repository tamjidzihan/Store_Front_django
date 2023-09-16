from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from decimal import Decimal
from .models import *



class CatagorySerializer(ModelSerializer):
    class Meta:
        model = Catagory
        fields = ['id','title','feature_product']
    
    feature_product = serializers.StringRelatedField()



class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','title','price','price_with_tax','description','catagory']

    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    catagory = serializers.HyperlinkedRelatedField(
        queryset = Catagory.objects.all(),
        view_name= 'catagory-detail'
    )

    def calculate_tax(self,product:Product):
        return product.price * Decimal(1.1)

    