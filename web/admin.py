from django.contrib import admin
from .models import (
    Staff, StaffCategory, FoodCategory, Food, Comment,
    Complaint, Contact, Room, RoomType, BookingOrder
)
    

# Register your models here.
class StaffAdmin(admin.ModelAdmin):
    list_display = ['staff_id', 'lname', 'category']

class FoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']


class ContactAdmin(admin.ModelAdmin):
    list_display = ['email', 'subject']

class RoomAdmin(admin.ModelAdmin):
    list_display = ['category', 'room_no', 'available']


class BookingOrderAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'checkin_date', 'checkout_date')

admin.site.register(Staff, StaffAdmin)
admin.site.register(StaffCategory)
admin.site.register(FoodCategory)
admin.site.register(Food, FoodAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(RoomType)
admin.site.register(BookingOrder, BookingOrderAdmin)
# admin.site.register(Guest)
