from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Book(models.Model):
#we are using inheritance by adding models.Model inside parenthesis
#we are using sql databases that are tablebased so, we will be storing values as id


 title=models.CharField(max_length=50)
 #we cannot directly give the values as it should be the blueprint for book instances which we create
 # charfield construct accepts several para to specify the behavior of field
 #so django will understand that if the book title will be created then it will be of text type and will not be too long


 rating= models.IntegerField(
 validators=[MinValueValidator(1),MaxValueValidator(5)])
 #validators=#validate the data before it is saved to the db in this case the rating should be between 1-5
 #no need to pass anything here like CharField
 #to set this to a number without any decimal places


 author=models.CharField(null=True,max_length=100)
 is_bestselling= models.BooleanField(default=False)#just to know whether the book is best selling or not


 #automatically the id column will be created by django
 #id=models.AutoField--can be used to create id manually
 
 def __str__(self):
  return f"{self.title}({self.rating})"