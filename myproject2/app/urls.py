from django.urls import path
from . import views
from .views import get1,get2,get4,get3

urlpatterns = [
    path('', get1, name='home'),  # Homepage accessible at "/"

    path('product/', views.product_list, name='product_list'),
    path('cart/', views.cart_view, name='cart_view'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('checkout/', views.checkout, name='checkout'),
    # path('home/',get1,name='home'),
    path('service/',get2,name='service'),
    path('contact/',get4,name='contact'),
    path('about/',get3,name='about'),
    # path('home/product/home',get1,name='home'),
    path('delete/<int:item_id>/', views.delete_cart_item, name='delete_cart_item'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('order/<int:order_id>/', views.order_confirmation, name='order_confirmation'),
    path('checkout/order/<int:order_id>', views.order_confirmation, name='order'),
    path('checkout/order/<int:order_id>', views.order_confirmation, name='order'),
    path('checkout/order_confirmation.html/<int:order_id>', views.order_confirmation, name='order'),
]



from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CartViewSet, OrderViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'carts', CartViewSet)
router.register(r'orders', OrderViewSet)



