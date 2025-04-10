from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile



@receiver(post_save, sender=User)
def post_save_receiver(sender, instance, created, **kwargs):
    if created:
        new_user = instance
        new_user_profile = Profile.objects.create(user=new_user)
        # new_user_profile.save()   No need of this line
        print("user created")
        
#sender = user model
#instance = User objects
#created = boolean value


# settings changed signals
def my_callback(sender, **kwargs):
    print("Setting changed!")