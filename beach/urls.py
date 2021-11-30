from django.urls import path
from . import views
from .models import Beach
# .  represents the current folder

#URLConf
urlpatterns = [
    path('', views.display),
    path('<beachName>/', views.display, name='beach'),
    path('<beachName>/average/', views.average)
]
