from django.urls import path
from web import  views


urlpatterns = [
    path('', views.index,  name='index'),
    path('accommodation', views.accommodation,  name='accommodation'),
    path('contact', views.contact,  name='contact'),
    path('success', views.success, name="success"),
    path('about', views.about, name="about"),
    path('roomdetail/<int:id>',views.room_detail , name='room_detail'),
    path('map', views.default_map, name="default")
    # path('room-success', views.booked_successfuly, name="room-success"),


]