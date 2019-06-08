from django.urls import path
from .views import firstTry, receive_tweet

urlpatterns = [
    path('home', firstTry, name='firsttry'),
    path('result', receive_tweet, name='tweet_submit'),
]
