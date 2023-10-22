from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Establece la hora actual usando la zona horaria definida en Django.
ahora = timezone.now()


# Modelo para el perfil del usuario.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Relación uno a uno con el modelo de usuario.
    position = models.CharField(max_length=100)  # Cargo o posición del usuario.
    image = models.ImageField(upload_to='profile_pics', default='default.jpg')  # Imagen de perfil con imagen predeterminada.


# Modelo para noticias.
class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()  # Contenido completo de la noticia.
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)  # Imagen opcional para la noticia.
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación de la noticia.

    def __str__(self):
        return self.title
    # Si deseas agregar más campos como autor o categorías, este es el lugar.


# Modelo para eventos.
class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Usuario relacionado con el evento.
    title = models.CharField(max_length=200)
    start_date = models.DateTimeField()  # Fecha y hora de inicio del evento.
    end_date = models.DateTimeField()  # Fecha y hora de finalización del evento.
    # Aquí puedes añadir más detalles como ubicación o descripción del evento.


# Modelo para solicitudes.
class Request(models.Model):
    # Define las opciones para tipos de solicitudes.
    REQUEST_CHOICES = (
        ('Vacaciones', 'Vacaciones'),
        ('Justificante absentismo', 'Justificante absentismo'),
        ('Permiso', 'Permiso'),
        ('Otras solicitudes', 'Otras solicitudes'),
    )
    # Define los estados de las solicitudes.
    PENDING = 'Pendiente'
    APPROVED = 'Aprobada'
    REJECTED = 'Rechazada'

    STATUS_CHOICES = (
        (PENDING, 'Pendiente'),
        (APPROVED, 'Aprobada'),
        (REJECTED, 'Rechazada'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=50, choices=REQUEST_CHOICES)
    start_date = models.DateField()  # Fecha de inicio de la solicitud.
    end_date = models.DateField()  # Fecha de finalización de la solicitud.
    description = models.TextField()  # Descripción detallada de la solicitud.
    document = models.FileField(upload_to='documents/', null=True, blank=True)  # Documento opcional adjunto.
    is_approved = models.BooleanField(default=False)  # Estado de aprobación.
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación de la solicitud.
    subject = models.CharField(max_length=200, default='Asunto no especificado')  # Asunto de la solicitud.
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="Pendiente")
    # Si planeas agregar algún tipo de seguimiento o comentarios, este es el lugar adecuado.


# Estas funciones crean y guardan el perfil del usuario automáticamente cuando se crea un nuevo usuario.
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



