from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy.api import API
from Hashtag.models import Hashtag
import TintProject.tasks
from celery import chord
# from tasks import display
# from TintProject.messaging import send_increment

import json

class listener(StreamListener):
    counter1 = long(0)
    counter2 = long(0)
    def __init__(self, str1,str2, api=None):
        self.api = api or API()
        self.str1 = str1        
        self.str2 = str2
        

    def on_data(self, data):

        data = json.loads(data)

        # Continue counting
        if self.str1 in data["text"]:

            # self.counter1 += 1
            # if self.counter1>=10:
                # chord(TintProject.tasks.update.apply_async(self.str1,10))
                # self.counter1 = 0
            
            h1 = Hashtag.objects.get(name = self.str1)
            h1.ct = h1.ct+1
            h1.save() 

        if self.str2 in data["text"]:

            # self.counter2 += 1
            # if self.counter2>=10:
                # chord(TintProject.tasks.update.apply_async(self.str2,10))
                # self.counter2 = 0

            h1 = Hashtag.objects.get(name = self.str2)
            h1.ct = h1.ct+1
            h1.save() 

        # chord(TintProject.tasks.update.apply_async((self.str1,self.counter1),countdown = 1))
        # chord(TintProject.tasks.update.apply_async((self.str2,self.counter2),countdown = 1))


        if  'in_reply_to_status' in data:
            self.on_status(data)        
        elif 'delete' in data:
            delete = json.loads(data)['delete']['status']
            if self.on_delete(delete['id'], delete['user_id']) is False:
                return False
        elif 'limit' in data:
            if self.on_limit(json.loads(data)['limit']['track']) is False:
                return False
        elif 'warning' in data:
            warning = json.loads(data)['warnings']
            print warning['message']
            return false

    def on_error(self,status):
        print 'error'
        print status
