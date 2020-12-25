from django import forms
from .models import Contact, BookingOrder
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

FOOD_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 11)]

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserLoginForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget = forms.PasswordInput)
    class Meta:
        model = User
        fields = ['email', 'password']

    def validate(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password = password):
                raise forms.ValidationError("Invalid login")


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

class CartAddFoodForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=FOOD_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)