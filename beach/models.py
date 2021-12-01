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
CHOICE_AVAILABLE = (
    ('Yes', 'Yes'), 
    ('No', 'No'))

CHOICE_NUM = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
    (7, '7'),
    (8, '8'),
    (9, '9'),
    (10, '10')
)
class Beach(models.Model):
    name = models.CharField(max_length = 60)
    img = models.ImageField(upload_to='beach_pic', null = True)
    
    region = models.CharField(max_length = 2, choices=CHOICE_REGIONS) # N, NE, E, SE, S, SW, W, NW
    #Ratings
    
    overallRating = models.DecimalField(max_digits=3, decimal_places=1, null = True, default=0)
    swimRating = models.DecimalField(max_digits=3, decimal_places=1, null = True, default=0)
    diveRating = models.DecimalField(max_digits=3, decimal_places=1, null = True, default=0)
    surfRating = models.DecimalField(max_digits=3, decimal_places=1, null = True, default=0)
    loungeRating = models.DecimalField(max_digits=3, decimal_places=1, null = True, default=0)
    boatRating = models.DecimalField(max_digits=3, decimal_places=1, null = True, default=0)
    isCleanRating = models.DecimalField(max_digits=3, decimal_places=1, null = True, default=0)
    safetyRating = models.DecimalField(max_digits=3, decimal_places=1, null = True, default=0)
    
    lifeguardRating = models.CharField(max_length = 3, choices=CHOICE_AVAILABLE, default= 'No')

    def __str__(self):
        return self.name
    

class Profile(models.Model):
    img = models.ImageField(upload_to='profile_pic', null = True)
    date_created = models.DateTimeField(default = timezone.now)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    bio = models.TextField(max_length=500, blank = True)
    bucketList = models.TextField(max_length=1000, blank = True)
    region = models.CharField(max_length = 2, choices=CHOICE_REGIONS) # N, NE, E, SE, S, SW, W, NW
    
    def __str__(self):
        return self.user.get_username()
    
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

class Rating(models.Model):
    #Ratings
    date_posted = models.DateTimeField(default = timezone.now)
    
    overall = models.PositiveIntegerField(null = True, default=10, choices=CHOICE_NUM)
    swim = models.PositiveIntegerField(blank = True, null=True, choices=CHOICE_NUM)
    dive = models.PositiveIntegerField(blank= True, null = True, choices=CHOICE_NUM)
    surf = models.PositiveIntegerField(blank= True, null = True, choices=CHOICE_NUM)
    lounge = models.PositiveIntegerField(blank= True, null = True, choices=CHOICE_NUM)
    boat = models.PositiveIntegerField(blank= True, null = True, choices=CHOICE_NUM)
    isClean = models.PositiveIntegerField(blank= True, null = True, choices=CHOICE_NUM)
    safety = models.PositiveIntegerField(blank= True, null = True, choices=CHOICE_NUM)
    lifeguard = models.CharField(max_length = 3, choices=CHOICE_AVAILABLE, default='No', null = True)
    #Rating belongs to beach:
    
    author = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    beach = models.ForeignKey(Beach, on_delete = models.CASCADE, null= True)
    
    def __str__(self):
            return 'Rating_' + str(self.beach.name) + '_' + str(self.author.get_username())

    
