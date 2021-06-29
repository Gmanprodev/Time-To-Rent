from django.apps import AppConfig

""" built in default field. """


class BagConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bag'
