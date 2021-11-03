from django.urls import path
from . import views
# .  represents the current folder

#URLConf
urlpatterns = [
    path('', views.home),
    path("reverseList", views.reverseList),
    path("undoReverse", views.undoReverse),
    path("sortBy/<type>", views.sortBy),
    path("sortByRegion/<region>", views.sortByRegion),
    path("showAllRegions", views.showAllRegions)
]