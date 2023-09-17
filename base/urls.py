from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('products/', views.product_list),
    path('products/<int:pk>', views.product_detail),

    path('catagory/', views.catagoty_list),
    path('catagory/<int:pk>', views.catagoty_detail,name='catagory-detail'),
]