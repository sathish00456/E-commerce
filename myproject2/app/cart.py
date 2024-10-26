# cart.py

from django.conf import settings

class Cart:
    def __init__(self, request):
        """Initialize the cart."""
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # Initialize an empty cart if none exists
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1):
        """Add a product to the cart or update its quantity."""
        product_id = str(product.id)
        if product_id in self.cart:
            # Update the quantity if the product already exists
            self.cart[product_id]['quantity'] += quantity
        else:
            # Add a new product to the cart
            self.cart[product_id] = {'quantity': quantity, 'price': str(product.price), 'image': str(product.image.url)}
        self.save()  # Save changes to the session

    def remove(self, product_id):
        """Remove a product from the cart."""
        if str(product_id) in self.cart:
            del self.cart[str(product_id)]
            self.save()  # Save changes to the session

    def get_total_price(self):
        """Calculate the total price of all items in the cart."""
        return sum(float(item['price']) * item['quantity'] for item in self.cart.values())

    def save(self):
        """Save the current cart state to the session."""
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True  # Mark the session as modified

    def clear(self):
        """Clear the cart."""
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True  # Mark the session as modified
