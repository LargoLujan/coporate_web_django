from django import forms
from .models import News, Request, Event, Profile
from django.contrib.auth.models import User, Group


# Esta es una forma para añadir o editar Noticias.
class NewsForm(forms.ModelForm):
    class Meta:
        model = News  # Modelo asociado a la forma
        fields = ['title', 'content', 'image']  # Campos del modelo que se quieren en el formulario
        # Widgets personalizados para el diseño del formulario
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
        }


# Esta es una forma para añadir o editar Solicitudes.
class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['request_type', 'start_date', 'end_date', 'description', 'document']
        widgets = {
            'request_type': forms.Select(choices=Request.REQUEST_CHOICES, attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'document': forms.FileInput(attrs={'class': 'form-control-file'}),
        }


# Esta es una forma para añadir o editar Eventos.
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'start_date', 'end_date']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'start_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'end_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }


POSITION_CHOICES = [
    ('employees', 'Employees'),
    ('admin', 'Admin'),
    ('head', 'Head'),
]


# Esta es una forma para actualizar el Perfil del usuario.
class ProfileUpdateForm(forms.ModelForm):
    # Se definen campos adicionales que no están directamente en el modelo Profile, pero se necesitan para actualizar
    # el usuario.
    user_first_name = forms.CharField(max_length=30, label="Nombre")
    user_last_name = forms.CharField(max_length=30, label="Apellidos")
    user_username = forms.CharField(max_length=30, label="Usuario")
    user_email = forms.EmailField(label="Correo")
    user_password = forms.CharField(widget=forms.PasswordInput(), required=False, label="Contraseña")
    position = forms.ModelChoiceField(queryset=Group.objects.all(), label="Posición/Grupo de trabajo")

    class Meta:
        model = Profile
        fields = ['image', 'user_first_name', 'user_last_name', 'user_username', 'user_email', 'user_password',
                  'position']


# Esta es una forma para actualizar los detalles del Usuario (modelo User).
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


# Esta es una forma para editar Solicitudes existentes.
class EditRequestForm(forms.ModelForm):
    status = forms.ChoiceField(choices=Request.STATUS_CHOICES)

    class Meta:
        model = Request
        fields = ['description', 'status']
