from django.urls import path

from userProfile.views import add
from . import views
from userProfile import views as profileView
# .  represents the current folder

#URLConf
urlpatterns = [
    path('', views.home, name = 'home'),
    path("reverseList", views.reverseList),
    path("undoReverse", views.undoReverse),
    path("sortBy/<type>", views.sortBy),
    path("sortByRegion/<region>", views.sortByRegion),
    path("showAllRegions", views.showAllRegions),
    path("add/<beachName>", profileView.add), #go to userProfile
]