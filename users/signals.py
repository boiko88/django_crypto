from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings

from .models import Profile


User = get_user_model()


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.create(user=instance)

        # Save the email to the profile (if provided)
        if instance.email:
            profile.email = instance.email
            profile.save()

            # Send welcome email
            send_mail(
                subject='🎉 Welcome to CryptoPlatform!',
                message='Thanks for joining CryptoPlatform. Enjoy exploring crypto rates, blogs, and more!',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[instance.email],
                fail_silently=False,
            )


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
