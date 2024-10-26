from rest_framework import serializers
from .models import Product, Cart, CartItem, Order, OrderItem

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'  # Or specify specific fields like ['id', 'name', 'description', 'price', 'image', 'stock']

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()  # Nesting the ProductSerializer to include product details

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'total_price']

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)  # Include cart items in the cart

    class Meta:
        model = Cart
        fields = ['id', 'user', 'created_at', 'items']

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()  # Nesting the ProductSerializer

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)  # Include order items in the order

    class Meta:
        model = Order
        fields = ['id', 'user', 'total_price', 'created_at', 'is_paid', 'order_items']
