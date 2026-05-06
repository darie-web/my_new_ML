from django.apps import AppConfig

class EndpointsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.endpoints'  # This must match how it's referenced in INSTALLED_APPS

