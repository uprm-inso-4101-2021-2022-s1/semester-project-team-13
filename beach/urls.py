from django.urls import path
from . import views
# .  represents the current folder

#URLConf
urlpatterns = [
    path('', views.display),
]