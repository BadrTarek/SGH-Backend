from django.apps import AppConfig

# from suit.apps import DjangoSuitConfig

# class SuitConfig(DjangoSuitConfig):
#     layout = 'horizontal'


class UsersappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Apps.Users'
