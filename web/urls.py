from django.urls import path
from web import  views
# from .views import SearchResultsView

urlpatterns = [
    path('', views.index,  name='index'),
    path('register', views.register,  name='register'),
    path('login', views.login,  name='login'),
    path('accommodation', views.accommodation,  name='accommodation'),
    path('contact', views.contact,  name='contact'),
    path('success', views.success, name="success"),
    path('about', views.about, name="about"),
    path('doublerooms/', views.doubleRoom, name="double-rooms"),
    path('singlerooms/', views.singleRoom, name="single-rooms"),
    path('sharedrooms/', views.sharedRoom, name="shared-rooms"),
    path('roomdetail/<int:id>',views.room_detail , name='room_detail'),
    path('search', views.search, name="search"),
    path('weather', views.currentWeather, name="weather"),
    path('food', views.food, name="food"),
    path('addtocart/<int:food_id>/', views.cart_add, name="add-to-cart"),
    path('removefromcart', views.cart_remove, name="remove-from-cart"),
    path('fooddetail/<int:id>',views.food_detail , name='food-detail'),
    path('cartdetail/',views.cart_detail , name='cart-detail'),

    # path('map', views.default_map, name="default")
    # path('room-success', views.booked_successfuly, name="room-success"),


]
# x = Room.objects.filter(category__category="single")