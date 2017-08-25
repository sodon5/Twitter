import codecs
import tweepy
import os
from datetime import datetime
from config import *

consumer_key='83l3Y60a7HLRxrCK08gjns4hi'
consumer_secret='ZnS8IXZqsmvFnpaYVhWbSZi8WA6IIzAuhgxqQRPo1nLSGI8wCr'
access_token='819093425676951553-QYr6aodqaJkHGYLd19u4SpEDFGm9cSq'
access_token_secret='WxInkEKEnUFbed6Mi0wQ6081S5C90blTOx8Jb6yQTPPtZ'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

class listener(tweepy.streaming.StreamListener):
    def on_data(self, data):

        try:
            data = data.encode('utf-8')
            data = data.decode('unicode_escape')
        except:
            print('Err')

        currentTime = datetime.now()
        currentHour = currentTime.hour

        if self.priorHour != currentHour:
                print("(!)--Hour change!! Current time is ", end="")
                print(currentTime.strftime("%Y-%m-%d %H:00"))
                self.file.close()
                if not os.path.exists("./data/"+currentTime.strftime("%Y-%m-%d")):
                    os.makedirs("./data/"+currentTime.strftime("%Y-%m-%d"))
                path = "./data/"+currentTime.strftime("%Y-%m-%d")+"/"+currentTime.strftime("%Y-%m-%d-%H")+".dat"
                self.file = open(path, "w", encoding='utf8')
                self.priorHour = currentHour
        print("tweet!")
        self.file.write(data)
        return True

    def on_error(self, status):
        print('error : ', status)

twitterStream = tweepy.Stream(auth, listener())
twitterStream.filter(track='파이썬')