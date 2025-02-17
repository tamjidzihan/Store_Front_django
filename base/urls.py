from django.urls import path,include
from rest_framework_nested import routers
from . import views


router =routers.DefaultRouter()
router.register('products',views.ProducViewset,basename='products')
router.register('catagory',views.CatagoryViewset)
router.register('cart',views.CartViewset)
router.register('customer',views.CustomerViwset)
router.register('order',views.OrderViewset,basename='order')
router.register('catagoryproduct',views.CatagoryProductViewSet, basename='catagoryproduct')



product_router =  routers.NestedDefaultRouter(router,'products',lookup = 'product')
product_router.register('like',views.LikeViewset,basename='product-like')
product_router.register('images',views.ProducImageViewset,basename='product-image')


cart_router = routers.NestedDefaultRouter(router,'cart',lookup = 'cart')
cart_router.register('cartitem',views.CartItemViewset,basename='cart-item')


order_router = routers.NestedDefaultRouter(router,'order',lookup= 'order')
order_router.register('orderitem',views.OrderItemViewset,basename='order-item')


urlpatterns = [
    # path('', views.index),
    path('',include(router.urls)),
    path('',include(product_router.urls)),
    path('',include(cart_router.urls)),
    path('',include(order_router.urls)),
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

