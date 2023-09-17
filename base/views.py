from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models.aggregates import Count
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
              if product.orderitem.count()>0:
                    return Response({'error':f'Product can not be deleted.Because Product is on orderitem.' },status=status.HTTP_405_METHOD_NOT_ALLOWED)
              product.delete()
              return Response({'Deleted Product id': pk},status=status.HTTP_204_NO_CONTENT)

   

@api_view(['GET','POST'])
def catagoty_list(request):
        if request.method == 'GET':
                queryset = Catagory.objects.annotate(product_count = Count('product')).all()
                serializer = CatagorySerializer(queryset,many = True,context={'request': request})
                return Response(serializer.data)
        elif request.method == 'POST':
                serializer = CatagorySerializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)



@api_view(['GET','PUT','DELETE'])
def catagoty_detail(request,pk):
        catagory = get_object_or_404(Catagory.objects.annotate(product_count = Count('product')), pk=pk)
        if request.method == 'GET':
                serializer = CatagorySerializer(catagory)
                return Response(serializer.data)
        elif request.method == 'PUT':
               serializer = CatagorySerializer(catagory,data=request.data)
               serializer.is_valid(raise_exception=True)
               serializer.save()
               return Response(serializer.data,status=status.HTTP_201_CREATED)
        elif request.method == 'DELETE':
               if catagory.product_set.count() >0:
                      return Response({'error':f'Catagory can not be deleted.Because it has Some product on it.' },status=status.HTTP_405_METHOD_NOT_ALLOWED)
               else:
                      catagory.delete()
                      return Response({'Deleted Catagory id': pk},status=status.HTTP_204_NO_CONTENT)

              


