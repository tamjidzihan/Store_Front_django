from django.urls import path,include
from rest_framework.routers import SimpleRouter,DefaultRouter
from . import views


router = SimpleRouter()
router.register('products',views.ProducViewset)
router.register('catagory',views.CatagoryViewset)


urlpatterns = [
    path('', views.index),
    path('',include(router.urls))
    
]







# urlpatterns = [
#     path('', views.index),
    # path('products/', views.product_list),
    # path('products/<int:pk>', views.product_detail),

    # path('catagory/', views.catagoty_list),
    # path('catagory/<int:pk>', views.catagoty_detail,name='catagory-detail'),

    # path('products/', views.ProductList.as_view()),
    # path('products/<int:pk>', views.ProductDetail.as_view()),

    # path('catagory/', views.CatagoryList.as_view()),
    # path('catagory/<int:pk>', views.CatagoryDetail.as_view(),name='catagory-detail'),
    
# ]