import tweepy

consumer_key='RTZ8N63pB2GaIYK5Ha4y3BA1L'
consumer_secret='etrQPZjH4fbLurdpm9QQMzb1J5ZKEtkTcnrKsUymtvnRW5YwyH'
access_token='818676214017572864-quoGgHv7F8S7PlFxZsKBh61tN0Eu2AI'
access_token_secret='vtjbMTt7zHu4K7LrIgSSYkMMJ80fEvYuZnRjX68HULzy8'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print (tweet.text)

# In this example, the handler is time.sleep(15 * 60),
# but you can of course handle it in any way you want.

def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(15 * 60)

for follower in limit_handled(tweepy.Cursor(api.followers).items()):
    if follower.friends_count < 300:
        print (follower.screen_name)