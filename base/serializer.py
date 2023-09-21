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
        fields = ["id","title","slug","inventory","price","price_with_tax","description","catagory"]

    price_with_tax = serializers.SerializerMethodField(method_name="calculate_tax")

    def calculate_tax(self, product: Product):
        return product.price * Decimal(1.1)


# __________________________________
# def validate(self, data):
#     if data['password'] != data['confirm_password']:
#         return serializers.ValidationError('Pass word do not match')
#     return data
# ____________________________________


class LikeSerializer(ModelSerializer):
    class Meta:
        model = Like
        fields = ['id','date','like','customer','product']

    def create(self, validated_data):
        product_id = self.context['product_id']
        return Like.objects.create(product_id = product_id,**validated_data)



class CartItemProduct(ModelSerializer):
    class Meta:
        model = Product
        fields = ['title','price']



class AddCartItemSerializer(ModelSerializer):
    product_id = serializers.IntegerField()

    def validate_product_id(self, value):
        if not Product.objects.filter(pk = value).exists():
            raise serializers.ValidationError('Invalide query')


    def save(self, **kwargs):
        cart_id = self.context['cart_id']
        product_id = self.validated_data['product_id']
        quantity = self.validated_data['quantity']

        try:
            cart_item =  CartItem.objects.get(cart_id = cart_id,product_id=product_id)
            cart_item.quantity += quantity
            cart_item.save()
            self.instance = cart_item
        except CartItem.DoesNotExist:
            self.instance = CartItem.objects.create(cart_id = cart_id,**self.validated_data)
        return self.instance


    class Meta:
        model = CartItem
        fields = ['id','product_id','quantity']



class CartItemSerializer(ModelSerializer):
    product = CartItemProduct()
    product_total_price = serializers.SerializerMethodField(method_name='calculate_total_price')

    def calculate_total_price(self,cart_item:CartItem):
        return cart_item.quantity * cart_item.product.price
    
    class Meta:
        model = CartItem
        fields = ['id','product','quantity','product_total_price']






class CartSerializer(ModelSerializer):
    cartitem_set = CartItemSerializer(read_only = True,many =True)
    id = serializers.UUIDField(read_only = True)
    cart_item_total_price = serializers.SerializerMethodField(method_name='get_cart_item_total_price')

    def get_cart_item_total_price(self,cart:Cart):
        total_price = []
        for items in cart.cartitem_set.all():
            total_price.append(items.quantity * items.product.price)
        return sum(total_price)

    class Meta:
        model= Cart
        fields = ['id','cartitem_set','cart_item_total_price']


    





