from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import datetime,date,timedelta
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.

class StaffCategory(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "StaffCategories"

class Staff(models.Model):
    staff_id = models.CharField(max_length=20, primary_key=True, unique=True, blank=False)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    category= models.ForeignKey(StaffCategory, on_delete=models.CASCADE)
    profilepic = models.ImageField(default='', upload_to='staff images')

class FoodCategory(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "Food Categories"
    
    def __str__(self):
        return self.name
    
class Food(models.Model):
    category= models.ForeignKey(FoodCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    food_image = models.ImageField(upload_to="room images", default="cook.jpeg")
    description = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=10)

    def get_absolute_url(self):
        return reverse('food-detail', args=[str(self.id)])
    
    
class Comment(models.Model):
    name = models.CharField(max_length=20)
    your_comment = models.TextField()

class Complaint(models.Model):
    name = models.CharField(max_length=20)
    your_complain = models.TextField()

class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()

class RoomType(models.Model):
    name =  models.CharField(max_length=20)
    description = models.TextField(default='gg')

    def __str__(self):
        return self.name

class Room(models.Model):
    category = models.ForeignKey(RoomType, on_delete=models.CASCADE, related_name="room_category" )
    room_no = models.CharField(max_length=5)
    Specifications = models.CharField(max_length=300, default="")
    available = models.BooleanField(default=False)
    room_img = models.ImageField(upload_to="room images")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)


    def get_absolute_url(self):
        return reverse('room_detail', args=[str(self.id)])

    def __str__(self):
        return self.room_no

# class Guest(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     first_name = models.CharField(max_length=20)
#     last_name = models.CharField(max_length=20)
#     email = models.EmailField(max_length=50)
#     age=models.IntegerField(default=20)
#     phone=models.CharField(max_length=10)

#     def __str__(self):
#         return self.email


class BookingOrder(models.Model):
    guest = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    checkin_date = models.DateTimeField(default=datetime.now())
    checkout_date = models.DateTimeField(default=datetime.now() + timedelta(days=1))
    checkout = models.BooleanField(default=False)
    no_of_guests=models.IntegerField(default=1)

    def __str__(self):
        return self.guest.email
    
    def charge(self):
        if self.checkout:
            if self.checkin_date == self.checkout_date:
                return self.room.price
            else:
                time_delta = self.checkout_date - self.checkin_date
                total_days_stayed = time_delta.days
                total_cost = self.room.price * total_days_stayed
                return total_cost
        else:
            return "Bill given when checking out"

@receiver(post_save, sender=BookingOrder)
def room_availability(sender, instance, created, **kwargs):
    room = instance.room
    if created:
        room.available = False
    room.save()
    if instance.checkout == True:
        room.available = True
    room.save()

    

