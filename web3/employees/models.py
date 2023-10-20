from datetime import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

ahora = timezone.now()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='profile_pics', default='default.jpg')

    def works_on(self, day):
        """Devuelve True si el usuario trabaja en el día especificado, de lo contrario, devuelve False."""
        try:
            work_day = UserWorkDay.objects.get(user=self.user, date=day)
            return work_day.is_working
        except UserWorkDay.DoesNotExist:
            return False


class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()


class Request(models.Model):
    REQUEST_CHOICES = (
        ('Vacation', 'Vacation'),
        ('Absence', 'Absence'),
        ('Leave', 'Leave'),
        ('Other', 'Other'),
    )
    PENDING = 'Pending'
    APPROVED = 'Approved'
    REJECTED = 'Rejected'

    STATUS_CHOICES = (
        (PENDING, 'Pending'),
        (APPROVED, 'Approved'),
        (REJECTED, 'Rejected'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=50, choices=REQUEST_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    document = models.FileField(upload_to='documents/', null=True, blank=True)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(max_length=200, default='Asunto no especificado')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="Pending")


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class UserWorkDay(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255, blank=True)  # Añadido
    date = models.DateField()
    is_working = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now)  # Añadido

    def save(self, *args, **kwargs):
        # Actualiza el full_name antes de guardar
        self.full_name = f"{self.user.first_name} {self.user.last_name}"
        super(UserWorkDay, self).save(*args, **kwargs)
