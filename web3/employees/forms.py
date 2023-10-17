from django import forms
from .models import News, Request, Event, Profile
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import PasswordChangeForm


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
        }


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['request_type', 'start_date', 'end_date', 'description', 'document']
        widgets = {
            'request_type': forms.Select(choices=Request.REQUEST_CHOICES, attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'document': forms.FileInput(attrs={'class': 'form-control-file'}),
        }


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'start_date', 'end_date']  # actualicé los nombres de los campos aquí
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'start_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'end_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            # He eliminado la descripción porque no está en tu modelo
        }


POSITION_CHOICES = [
    ('employees', 'Employees'),
    ('admin', 'Admin'),
    ('head', 'Head'),
]


# forms.py


class ProfileUpdateForm(forms.ModelForm):
    user_first_name = forms.CharField(max_length=30, label="Nombre")
    user_last_name = forms.CharField(max_length=30, label="Apellidos")
    user_username = forms.CharField(max_length=30, label="Usuario")
    user_email = forms.EmailField(label="Correo")
    user_password = forms.CharField(widget=forms.PasswordInput(), required=False, label="Contraseña")
    position = forms.ModelChoiceField(queryset=Group.objects.all(), label="Posición/Grupo de trabajo")

    class Meta:
        model = Profile
        fields = ['image', 'user_first_name', 'user_last_name', 'user_username', 'user_email',
                  'user_password', 'position']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


'''class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['birthdate', 'position', 'image']'''
