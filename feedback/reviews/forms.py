#this file is created because manual handling of form is tough 
#no impact in db
from django import forms
from .models import Review
# class ReviewForm(forms.Form):
#     user_name= forms.CharField(label="YOUR NAME",max_length=100,error_messages={
#       "required":"Your name must not be empty!",
#       "max_length":"please enter a shorter name!"
#     })
#     review_text= forms.CharField(label="Your Feedback",widget=forms.Textarea,max_length=200)
#     rating= forms.IntegerField(label="Your Rating",min_value=1,max_value=5)


class ReviewForm(forms.ModelForm):#it is also used in template and django will automatically connect it to a model and take its input as field here
    class Meta:
        model = Review #connects review form to review model
        fields= "__all__" #to include all the fields from model
        #if only selected fields are required then fields= ['user_name','review_text','rating']
        #exclude=[all the field that you dont want to include]-- alternative approach used in case included data>excluded data
        labels={
            "user_name": "Your Name",
            "review_text": "Your Feedback",
            "rating": "Your Rating",
        }
        error_messages={
            "user_name":{     
                "required":"Your name must not be empty!",
                "max_length":"please enter a shorter name!"
            }
        }