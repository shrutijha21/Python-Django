from django.urls import path
from . import views
urlpatterns=[
    path("", views.ReviewView.as_view()),#built in method as we are extending a build in view class in views.py
    path("thank-you",views.thank_you),
]