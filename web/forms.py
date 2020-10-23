from django import forms
from .models import Contact, BookingOrder

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['email', 'subject', 'message']

     

class ReserveRoom(forms.ModelForm):
    class Meta:
        model =  BookingOrder
        fields = '__all__'
        

        widgets = {
            'fname': forms.TextInput(attrs={'class': 'formcontrol'}),
            'lname': forms.TextInput(attrs={'class': 'formcontrol'}),
            'email': forms.EmailInput(attrs={'class': 'formcontrol'}),
            'from_date': forms.DateTimeInput(attrs={'class': 'formcontrol'}),
            'to_date': forms.DateTimeInput(attrs={'class': 'formcontrol'}),
        }

        labels = {
            'fname': ('First Name'),
            'lname': ('Last Name'),
            'email': ('Email'), 
        }
