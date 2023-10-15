from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class UserProfile(models.Model):
    #image = models.FileField(upload_to = "data")
    #it is not really a user profile as it will only have a file image
    '''' image = models.FileField(upload_to = "data")# a filefield wants a file but this file will not be stored in a database as it is a bad practice to store a file in db
    so a file field will store the data in harddrive and only store the path of data in db
    upload_to"x" : it is used to tell that where the data is being stored but jango will ook for the x totally outside our django project.. and change the setting in settings.py and add the location '''
    image = models.ImageField(upload_to = "data")