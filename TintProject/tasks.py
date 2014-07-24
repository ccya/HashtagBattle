from celery import app
from Hashtag.models import Hashtag
from listener import listener
from tweepy import OAuthHandler
from tweepy import Stream
from celery import chord



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

@app.task
def update(str1,ct):
	h1 = Hashtag.objects.get(name =str1)
	h1.ct = ct
	h1.save() 

@app.task
def revoke_worker():
	app.control.revoke('1234', terminate=True)

