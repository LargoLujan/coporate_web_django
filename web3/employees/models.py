from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='profile_pics', default='default.jpg')


class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='news_pics', null=True, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)


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

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=50, choices=REQUEST_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    document = models.FileField(upload_to='documents/', null=True, blank=True)
    is_approved = models.BooleanField(default=False)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
