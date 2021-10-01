from django.db import models
from django.db.models.deletion import CASCADE, PROTECT
from django.utils import timezone
#Extends user
from django.contrib.auth.models import User

#Models are tables that will be stored in a database
#https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#proxy

CHOICE_REGIONS = (
        ('N', 'North'),
        ('NE', 'North East'),
        ('E', 'East'),
        ('SE', 'South East'),
        ('S', 'South'),
        ('SW', 'South West'),
        ('W', 'West'),
        ('NW', 'North West'),
    )
class Beach(models.Model):
    name = models.CharField(max_length = 60)
    #img = models.ImageField()
    
    region = models.CharField(max_length = 2, choices=CHOICE_REGIONS) # N, NE, E, SE, S, SW, W, NW
    #Ratings
    swimming = models.PositiveIntegerField()
    
    def __str__(self):
        return self.name
    

class Profile(models.Model):
    #img = models.ImageField(upload_to='profile_pic', default='default_user_pic.jpg')
    date_created = models.DateTimeField(default = timezone.now)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    bio = models.TextField(max_length=500, blank = True)

    region = models.CharField(max_length = 2, choices=CHOICE_REGIONS) # N, NE, E, SE, S, SW, W, NW
    def __str__(self):
        return 'Profile #' + str(self.user.id)
    
class Comment(models.Model):
    
        content = models.TextField()
        #Date posted in date format
        date_posted = models.DateTimeField(default = timezone.now)
        #The author, identified by django.contrib.auth.models. A user database is built into django
        author = models.ForeignKey(User, on_delete = models.CASCADE)
        #The beach this comment belongs to
        beach = models.ForeignKey(Beach, on_delete = models.CASCADE, null= True)

        def __str__(self):
            return 'Comment_#' + str(self.id) + '_' + self.beach.name



    
