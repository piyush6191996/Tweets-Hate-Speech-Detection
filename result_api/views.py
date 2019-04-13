from django.http import HttpResponse
from django.shortcuts import render
from hatesonar import Sonar
import json

# Create your views here.


def firstTry(request):
    return render(request, 'result_api/result_page.html')

def receive_tweet(request):
    tweet = request.GET.get('tweet')
    print(tweet)
    tweet = repr(tweet)
    sonar = Sonar()
    result = sonar.ping(text=tweet)
    print(result)
    json_result = json.dumps(result)
    return render(request, 'result_api/final_result1.html', result)
