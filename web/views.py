from django.shortcuts import render, redirect
from .forms import ContactForm, ReserveRoom
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .models import Room, Booking

# Create your views here.
def  index(request):
    return render(request, 'index.html')

def accommodation(request):
    rooms = Room.objects.filter(available=True)
    return render(request, 'accommodation.html', {'rooms': rooms})  
     
     
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
            # return redirect ("booked_successfuly")
    else:
        booking_form = ReserveRoom()
    return render(request, "room_detail.html", {'room_detail':room_detail, 'booking_form': booking_form})



                 
# def booked_successfuly(request):
#     return HttpResponse("You have succesfully booked a room")