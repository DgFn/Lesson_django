from django.apps import AppConfig


class TmsAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tms_app'
    def ready(self):
        from .signals import signal