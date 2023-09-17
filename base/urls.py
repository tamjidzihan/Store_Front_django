from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    # path('products/', views.product_list),
    # path('products/<int:pk>', views.product_detail),

    path('products/', views.ProductList.as_view()),
    path('products/<int:pk>', views.ProductDetail.as_view()),

    path('catagory/', views.catagoty_list),
    path('catagory/<int:pk>', views.catagoty_detail,name='catagory-detail'),
]