from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import ListView
from django.contrib import messages
import requests
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST

from .forms import ContactForm, ReserveRoom, UserRegisterForm, UserLoginForm, CartAddFoodForm
from .models import Room, BookingOrder, RoomType, Food
from .cart import Cart

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account created successfully for ' + user)
            return redirect('login')
    else:

        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    user = request.user
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(Email=email, password=password)
            if user:
                login(request, user)

        return redirect('index')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'user': user, 'form': form})
    # if user.is_authenticated:
    #     return redirect('index')
def logout(request):
    logout(request)
    return redirect('index')
            
def  index(request):
    return render(request, 'index.html')

def accommodation(request):
    rooms = Room.objects.filter(available=True)
    return render(request, 'accommodation.html', {'rooms': rooms})  

def doubleRoom(request):
    double_room = Room.objects.filter(category__name="Double")
    return render(request, 'double_room.html', {'double_room': double_room})

def singleRoom(request):
    single_room = Room.objects.filter(category__name="Single")
    return render(request, 'single-rooms.html', {'single_room': single_room})

def sharedRoom(request):
    shared_room = Room.objects.filter(category__name="Shared")
    return render(request, 'shared-room.html', {'shared_room': shared_room})
     
def  contact(request):
    if request.method == 'POST':
        form =  ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            print(form)
            form.save()
            try:
                send_mail(subject, message, email, ['chepngetichrose2030@gmail.com'])
            except BadHeaderError:
                return HttpResponseRedirect("Invalid header found")
            return redirect("success")
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def success(request):
    return HttpResponse("success, Thank you for your message.")

def about(request):
    mapbox_access_token = 'pk.my_mapbox_access_token'
    return render(request, 'about.html', { 'mapbox_access_token': mapbox_access_token })


def  room_detail(request, id):
    user = request.user
    room_detail = Room.objects.get(id=id)

    if request.method == 'POST':
        booking_form  = ReserveRoom(request.POST, instance=request.user)
        if booking_form.is_valid():
            # print(booking_form)
            booking_form.save()
            if booking_form:
                subject = 'Room Booking'
                message = 'You have successfully booked a room. \n Enjoy your stay with us'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = ['chepngetichrose2030@gmail.com', ]
                fail_silently = False
                mail_sent = send_mail(subject, message, email_from, recipient_list)
                room_detail.available = False
                print(mail_sent)
                return HttpResponse("Room booked succesfully")
            else:
                return HttpResponse("Please try again")
           
    else:
        booking_form = ReserveRoom()
    return render(request, "room_detail.html", {'room_detail':room_detail, 'booking_form': booking_form})

def sign_out(request):
    if request.method == 'POST':
        form = ReserveRoom(request.POST, request.instance)
                 
# def booked_successfuly(request):
#     return HttpResponse("You have succesfully booked a room")

def search(request):
    rooms = Room.objects.all()
    if request.method == 'POST':
        search = request.POST['search']
        print(search)
        rooms = Room.objects.filter(Q(room_category__icontains=search) | Q(Specifications__icontains=search))
    return render(request, 'search_results.html', {'rooms': rooms })
    
# class SearchResultsView(ListView):
#     model = Room
#     template_name = 'search_results.html'

#     def get_queryset(self): 
#         query = self.request.GET.get('q')
#         object_list = Room.objects.filter(
#             Q(category__icontains=query) | Q(Specifications__icontains=query)
#         )
#         return object_list

def currentWeather(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=f500a83d26ef9fae7f96ba796810dc17'
    city = 'Kapsoit'
    city_weather = requests.get(url.format(city)).json()
    print(city_weather)
    weather = {
        'city' : city,
        'temperature' : city_weather['main']['temp'],
        'description' : city_weather['weather'][0]['description'],
        'icon' : city_weather['weather'][0]['icon']
    }
    return render(request, 'weather.html', {'weather': weather})

def food(request):
    foods = Food.objects.all()
    return render(request, 'food.html', {'foods': foods})

def food_detail(request, id):
    food_detail = Food.objects.get(id=id)
    form = CartAddFoodForm()
    return render(request, 'food-detail.html', {'food_detail': food_detail, 'form': form})


#Adding food to cart
@require_POST
def cart_add(request, food_id):
    cart = Cart(request)
    food = get_object_or_404(Food, id=food_id)
    form = CartAddFoodForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add_food(food=food, quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect('cart-detail')


#removing food from the cart
def cart_remove(request, food_id):
    cart = Cart(request)
    food = get_object_or_404(Food, id=food_id)
    cart.remove(food)
    return redirect('cart-detail')

def cart_detail(request):
    cart = Cart(request)
    print(cart)
    # for item in cart:
    #     item['update_quantity_form'] = CartAddFoodForm(
    #         initial = {'quantity': item['quantity'],
    #         'update': True}
    #     )
    # , {'cart': cart}
    return render(request, 'cart-detail.html')

