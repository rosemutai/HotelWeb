from django.contrib import admin
from .models import Staff, StaffCategory, MenuCategory, Menu, Comment, Complaint, Contact, Room, RoomType, Booking

# Register your models here.
class StaffAdmin(admin.ModelAdmin):
    list_display = ['staff_id', 'lname', 'category']

class MenuAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']


class ContactAdmin(admin.ModelAdmin):
    list_display = ['email', 'subject']

class RoomAdmin(admin.ModelAdmin):
    list_display = ['category', 'room_no', 'available']

admin.site.register(Staff, StaffAdmin)
admin.site.register(StaffCategory)
admin.site.register(MenuCategory)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(RoomType)
admin.site.register(Booking)