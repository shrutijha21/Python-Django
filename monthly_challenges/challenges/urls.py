from django.urls import path
from . import views
urlpatterns=[#list created to store urls
    # path("january", views.january),
    # #the url could have been challenges\january but we wrote only january
    # #vies.index meand i am calling index function from views.py
    # #this function is created and imported just to tell django that i am giving two parameters here:
    # #1st to we give the url 
    # #2nd para is the response that will happen after we touch url
    # path("february", views.february),
    # path("march", views.march)
    path("",views.index,name="index"),#\challenges--pointed
    path("<int:month>",views.monthly_challenges_number),
    path("<str:month>",views.monthly_challenges,name="month-challenge")#this is created to avoid error in url name as we have manually created url in app
    #str show whatever we give should be treated as string
]