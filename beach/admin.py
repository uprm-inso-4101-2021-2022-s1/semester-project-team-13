from django.contrib import admin
from .models import Comment, Beach, Profile,Rating


# Register your models here.
admin.site.register(Comment)
admin.site.register(Beach)
admin.site.register(Profile)
admin.site.register(Rating)
