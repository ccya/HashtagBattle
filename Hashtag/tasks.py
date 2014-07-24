# from __future__ import absolute_import
from celery import app
from django.http import HttpResponse,Http404
from django.shortcuts import render
from Hashtag.models import Hashtag
from djcelery.models import PeriodicTask
# from TintProject.massging import process


@app.task
def display(str1,str2,request):
	print 'startTask'
	hashtag1 = Hashtag.objects.filter(name = str1)[0]
	hashtag2 = Hashtag.objects.filter(name = str2)[0]
	return render(request, 'search_results.html',
                {'hashtag1': hashtag1, 'hashtag2': hashtag2})

