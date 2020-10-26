from django.db import models
from django.utils.timezone import now
import datetime
from django.urls import reverse
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

class MenuCategory(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "MenuCategories"
    
    def __str(self):
        return self.name
    
class Menu(models.Model):
    category= models.ForeignKey(MenuCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=10)

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
    category = models.ForeignKey(RoomType, on_delete=models.CASCADE, related_name="category" )
    room_no = models.CharField(max_length=5)
    Specifications = models.CharField(max_length=300, default="")
    available = models.BooleanField(default=False)
    room_img = models.ImageField(upload_to="room images")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)


    def get_absolute_url(self):
        return reverse('room_detail', args=[str(self.id)])

    def __str__(self):
        return self.room_no

class BookingOrder(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.EmailField()
    from_date = models.DateTimeField(default=datetime.date.today)
    to_date = models.DateTimeField(blank=True, null=True, default =datetime.date.today)


    

