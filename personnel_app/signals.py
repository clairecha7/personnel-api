from django.contrib.auth.models import User
from .models import Personnel
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save

@receiver(post_save, sender = Personnel)
def check_staff_status(sender, instance, **kwargs):
    if instance.is_staff:
        User.objects.create(username=instance.email, email=instance.email, first_name = instance.first_name, last_name = instance.last_name, is_staff = True, password = "qazqwe123")