from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#Models are tables that will be stored in a database
class Comment(models.Model):
    #Text a.k.a the comment itself
    content = models.TextField()
    #Date posted in date format
    date_posted = models.DateTimeField(default = timezone.now)
    #The author, identified by django.contrib.auth.models. A user database is built into django
    author = models.ForeignKey(User, on_delete = models.CASCADE)

# class Profile(models.Model):
#     img = models.ImageField()
#     date_created = models.DateTimeField(default = timezone.now)
#     user = models.ForeignKey(User, on_delete= models.CASCADE)


    # def __str__(self):
    #     return User.username
