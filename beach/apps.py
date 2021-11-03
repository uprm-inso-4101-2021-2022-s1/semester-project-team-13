from django.apps import AppConfig
from django.template.defaulttags import register

class BeachConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'beach'

#Register any special filters here (for front end)
@register.filter
def get(dictionary, key):
    return dictionary.get(key)