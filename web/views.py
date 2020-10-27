from django.shortcuts import render, redirect
from .forms import ContactForm, ReserveRoom
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .models import Room, BookingOrder, RoomType
from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import ListView
import requests
# Create your views here.
def  index(request):
    return render(request, 'index.html')

def accommodation(request):
    rooms = Room.objects.filter(available=True)
    return render(request, 'accommodation.html', {'rooms': rooms})  

def doubleRoom(request, double):
    double_room = Room.objects.filter(category=double)
    return render(request, 'double_room.html', {'double_room': double_room})
     
     
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
    room_detail = Room.objects.get(id=id)

    if request.method == 'POST':
        booking_form  = ReserveRoom(request.POST)
        if booking_form.is_valid():
            print(booking_form)
            booking_form.save()
            if booking_form:
                subject = 'Room Booking'
                message = 'You have successfully booked a room. \n Enjoy your stay with us'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = ['chepngetichrose2030@gmail.com', ]
                fail_silently = False
                mail_sent = send_mail(subject, message, email_from, recipient_list)
                print(mail_sent)
            else:
                pass
            # return redirect ("booked_successfuly")
    else:
        booking_form = ReserveRoom()
    return render(request, "room_detail.html", {'room_detail':room_detail, 'booking_form': booking_form})

                 
# def booked_successfuly(request):
#     return HttpResponse("You have succesfully booked a room")

# def search(request):
#     rooms = Room.objects.filter(~Q(room_img=''))
#     if request.method == 'POST':
#         search = request.POST['search']
#         print(search)
#         rooms = Room.objects.filter(~Q(room_img='') & Q(room_Specifications__icontains=search))
#     return render(request, 'search_results.html', {'rooms': rooms })
class SearchResultsView(ListView):
    model = Room
    template_name = 'search_results.html'

    def get_queryset(self): 
        query = self.request.GET.get('q')
        object_list = R.objects.filter(
            Q(name__icontains=query) | Q(state__icontains=query)
        )
        return object_list

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