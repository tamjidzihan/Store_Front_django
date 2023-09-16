from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from.serializer import *

# Create your views here.

@api_view(['GET','POST'])
def product_list(request):
    if request.method == 'GET':
        queryset = Product.objects.select_related('catagory').all()
        serializer = ProductSerializer(queryset, many = True,context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('ok')
          
        



@api_view()
def product_detail(request,pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product,context={'request': request})
        return Response(serializer.data)
   

@api_view()
def catagoty_list(request):
        queryset = Catagory.objects.all()
        serializer = CatagorySerializer(queryset,many = True,context={'request': request})
        return Response(serializer.data)



@api_view()
def catagoty_detail(request,pk):
        catagory = get_object_or_404(Catagory, pk=pk)
        serializer = CatagorySerializer(catagory)
        return Response(serializer.data)