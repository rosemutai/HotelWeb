from decimal import Decimal
from django.conf import settings
from .models import Food

class Cart(object):
    #initialize cart
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
    
    def add_food(self, food, quantity=1, update_quantity=False):
        #Add product to the cart or update its quantity
        food_id = str(food.id)
        if food_id not in self.cart:
            self.cart[food_id] = {'quantity': 0, 'price': str(food.price)}
        if update_quantity:
            self.cart[food_id] [quantity] = quantity
        else:
            self.cart[food_id]['quantity'] += quantity
        self.save()
    
    def save(self):
        #update session cart
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True
    

    def remove_food(self):
        food_id = str(food.id)
        if food_id in self.cart:
            del self.cart[food_id]
            self.save()

def __iter__self(self):
    #iterate over the food in the cart and grt them from the db
    food_ids = self.cart.keys()
    #get the food objects and add them to the cart
    foods = Food.objects.filter(id__in=food_ids)
    for food in foods:
        self.cart[str(food.id)]['food'] = food
    for item in self.cart.values():
        item['price'] = Decimal(item['price'])
        item['total_price'] = item['price'] * item['quantity']
        yield item

def __len__(self):
    #count all items in the cart
    return sum(item['quantity'] for item in self.cart.values())

def get_total_price(self):
    return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

#remove cart from session
def clear(self):
    del self.session[settings.CART_SESSION_ID]
    self.session.modified = True

    



















