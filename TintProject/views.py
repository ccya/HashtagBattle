from django.http import HttpResponse,Http404
from django.shortcuts import render
# from django.template.loader import get_template
from Hashtag.models import Hashtag
from listener import listener
from tweepy import OAuthHandler
from tweepy import Stream
from celery import chord
from TintProject.tasks import revoke_worker
from TintProject.tasks import collect
from TintProject.tasks import update
from celery import chord
from django.http import HttpResponse


def display(request):
        if 'hashtag1' in request.GET and request.GET['hashtag1']:
            hashtag1str = request.GET['hashtag1'] 
        if 'hashtag2' in request.GET and request.GET['hashtag2']:
            hashtag2str = request.GET['hashtag2']
            hash1 = Hashtag.objects.get(name = hashtag1str)
            hash2 = Hashtag.objects.get(name = hashtag2str)
            # print hash1.ct
            # print hash2.ct
            per = (100.0*hash1.ct)/(hash1.ct+hash2.ct) if (hash1.ct+hash2.ct!=0) else 0.0
            # print per
            return render(request,'search_results.html',
                {'hashtag1': hash1, 'hashtag2': hash2,'per': per})
        else:
            return HttpResponse("ERROR")

def start(request):
    if 'hashtag1' in request.GET and request.GET['hashtag1']:
        hashtag1 = request.GET['hashtag1'] 
        if 'hashtag2' in request.GET and request.GET['hashtag2']:
            hashtag2 = request.GET['hashtag2']
            # Create new object if not exist
            h1 = Hashtag.objects.filter(name = hashtag1)
            if not h1:
                newhash1 = Hashtag(name = hashtag1, ct = 0)
                newhash1.save()
            else:
                h1[0].ct = 0
                h1[0].save()
            h2 = Hashtag.objects.filter(name = hashtag2)
            if not h2:
                newhash2 = Hashtag(name = hashtag2, ct = 0)
                newhash2.save() 
            else:
                h2[0].ct = 0
                h2[0].save()
            collect.apply_async((hashtag1,hashtag2),task_id = '1234',countdown = 1)
            return display(request)
    else:
        return HttpResponse("Not Enought Hashtags")

def revoke(request):
    revoke_worker.apply_async(countdown=1)
    return HttpResponse("worker closed")

def search_form(request):
    return render(request, 'search.html')






