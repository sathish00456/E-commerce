from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Cart, CartItem, Order, OrderItem
from django.contrib.auth.decorators import login_required

# General page views
def get1(request):
    return render(request, "index.html")

def get2(request):
    return render(request, "service.html")

def get3(request):
    return render(request, "about.html")

def get4(request):
    return render(request, "contact.html")

# Product listing
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product.html', {'products': products})

# Add product to cart
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    # Get or create a cart for the user
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    # Get or create a cart item for this product
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    
    # Increment the quantity if the item already exists
    if not created:
        cart_item.quantity += 1
    
    cart_item.save()
    return redirect('cart_view')

# View cart
@login_required
def cart_view(request):
    # Fetch the user's cart and associated cart items
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    return render(request, 'card.html', {'cart_items': cart_items})

# Checkout view
@login_required
def checkout(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)

    if request.method == "POST":
        # Create an order for the user
        order = Order.objects.create(user=request.user, total_price=sum(item.total_price for item in cart_items))
        
        # Transfer all items from the cart to the order
        for item in cart_items:
            OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity)
        
        # Clear the cart after checkout
        cart_items.delete()  # Deletes all CartItems
        return redirect('order_confirmation.html',)

    return render(request, 'checkout.html', {'cart_items': cart_items})

# Delete cart item
@login_required
def delete_cart_item(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    return redirect('cart_view')


def order_confirmation(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, 'order_confirmation.html', {'order': order})





from rest_framework import viewsets
from .models import Product, Cart, Order
from .serializers import ProductSerializer, CartSerializer, OrderSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer



from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Register View
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is already taken.')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email is already in use.')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                messages.success(request, 'Account created successfully!')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match.')
    return render(request, 'register.html')


 # Assuming you have an Order model

def order_confirmation(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, 'order_confirmation.html', {'order': order})

    
# Login View
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home page or dashboard
        else:
            messages.error(request, 'Invalid credentials.')
    return render(request, 'login.html')

# Logout View
def logout_view(request):
    logout(request)
    return redirect('login')

from django.shortcuts import redirect

def some_view(request):
    # Some logic here
    return redirect('home') 

