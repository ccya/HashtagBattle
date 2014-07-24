from celery import app
from Hashtag.models import Hashtag
from listener import listener
from tweepy import OAuthHandler
from tweepy import Stream
from celery import chord

"""
	In this file, I put all the celery task here. 'app' is an instance of Celery specified 
	in celery.py usign @app.task decorator means to register this task under 'app' instance.
	So that tasks will be recognized when being called.

"""

"""
	In this function, using the specified token, I create a connection using twitter's 
	streaming api. With this streaming api, we can collect the twitter that contains the 
	hashtag specified in 'track' arg. This connection wont be closed until the corresponding
	worker has been shut down by revoke function in views.py.
"""

@app.task
def collect(hashtag1,hashtag2):
	ckey = 'YyVlva7vgqsOde8ldC7hv8zv4'
	csecret = 'OJWEsSDIZv2oqGdwSfXq2ixj2vYccaGgCyXcA87bVLHAbmKRXM'
	atoken = '1260716269-kCBeHaWD63ZINkxTvd2kmqiNMiBSLt7tKDak93T'
	asecret = 'LczOksLgR9rYPl7BLIHTV38ptRfa1ZsmUbrRawvdbvvkr'
	auth = OAuthHandler(ckey,csecret)
	auth.set_access_token(atoken, asecret)
	twitterStream = Stream(auth,listener(hashtag1,hashtag2))
	twitterStream.filter(track =[hashtag1,hashtag2])

"""
	For this task,it's simply to update the database according to the params. In my initial
	design, updating tasks will be queued by celery task scheduler. When a free worker see the
	queued update task, that's when the actual update happens. But many problems has been caused
	by this approach. More details in section 'Future Work' of my report.

"""
@app.task
def update(str1,ct):
	h1 = Hashtag.objects.get(name =str1)
	h1.ct = ct
	h1.save() 

"""
	For this task, it will send a terminate signal to the collect-twitter-worker when being 
	called.
"""
@app.task
def revoke_worker():
	app.control.revoke('1234', terminate=True)

