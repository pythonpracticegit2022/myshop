from django.apps import AppConfig
from django.core.signals import setting_changed
# from .signals import my_callback


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        # implicit signal registration
        from . import signals

        # explicit way
        # post_save.connect(post_save_receiver)

        # setting_changed.connect(my_callback)