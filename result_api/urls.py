from django.urls import path
from .views import firstTry, receive_tweet

urlpatterns = [
    path('firsttry', firstTry, name='firsttry'),
    path('tweetsubmit', receive_tweet, name='tweet_submit'),
]
