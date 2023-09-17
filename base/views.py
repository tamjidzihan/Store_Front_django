from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from.serializer import *

# Create your views here.

def index(request):
      return render(request,'index.html')



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
        return Response(serializer.data,status=status.HTTP_201_CREATED)
          
        



@api_view(['GET','PUT','DELETE'])
def product_detail(request,pk):
        product = get_object_or_404(Product, pk=pk)
        if request.method == 'GET':    
                serializer = ProductSerializer(product,context={'request': request})
                return Response(serializer.data)
        elif request.method == 'PUT':
              serializer = ProductSerializer(product,data=request.data)
              serializer.is_valid(raise_exception=True)
              serializer.save()
              return Response(serializer.data,status=status.HTTP_201_CREATED)
        elif request.method == 'DELETE':
              if product.orderitem_set.count()>0:
                    return Response({'error':f'Product can not be deleted.Product is on order. Product id : {pk}' },status=status.HTTP_405_METHOD_NOT_ALLOWED)
              product.delete()
              return Response({'Deleted Product id': pk},status=status.HTTP_204_NO_CONTENT)

   

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