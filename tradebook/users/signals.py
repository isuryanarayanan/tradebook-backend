from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from users.models import User
from users.models import InvestorProfile
from users.models import AdministratorProfile


@receiver(post_save, sender=User)
def create_profile(sender, instance=None, created=False, **kwargs):
    if created:
        if instance.mode == 1:
            customer =InvestorProfile.objects.create(user=instance)
        if instance.mode == 2:
            vendor =AdministratorProfile.objects.create(user=instance)
