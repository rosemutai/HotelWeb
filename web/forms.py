from django import forms
from .models import Contact, Booking

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['email', 'subject', 'message']

     

class ReserveRoom(forms.ModelForm):
    class Meta:
        model =  Booking
        fields = '__all__'
        

        widgets = {
            'fname': forms.TextInput(attrs={'class': 'formcontrol'}),
            'lname': forms.TextInput(attrs={'class': 'formcontrol'}),
            'email': forms.EmailInput(attrs={'class': 'formcontrol'}),
            'start_date': forms.DateTimeInput(attrs={'class': 'formcontrol'}),
            'end_date': forms.DateTimeInput(attrs={'class': 'formcontrol'}),
        }

        labels = {
            'fname': ('First Name'),
            'lname': ('Last Name'),
            'email': ('Email'), 
        }
