from django.urls import path
from . import views
urlpatterns=[
    path("", views.ReviewView.as_view()),#built in method as we are extending a build in view class in views.py
    path("thank-you",views.ThankYouView.as_view()),
    path("reviews",views.ReviewsListView.as_view()),
    path("reviews/<int:pk>",views.SingleReviewView.as_view())#pk is use to tell django automatically that whatever we entered is primary key and shuld be used as an id
]