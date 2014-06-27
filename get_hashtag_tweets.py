import sys
import tweepy
import webbrowser

CONSUMER_KEY = 'p0eq8NMKUmBQGJDugMNpW1hb8'
CONSUMER_SECRET = 'eKgaNjZh3kUCSB8VwAItsYGpg3eZ1rUNY21PjvYihvWwzPpRTG'
ACCESS_KEY = '40087586-E2lSs4DOYf7yzFFlB66glfOdKG1i71CBgnXY6BCDS'
ACCESS_SECRET = 'hjHEUP54AV2sEAS9xrxSbR9hm0Z34ClNC6DQyXzP9JY48'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.secure = True
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
tweets = []

tag = raw_input('Hashtag: ').strip()

for status in tweepy.Cursor(api.search, q=tag, locale='en',).items():
    #print status.user.name, '@'+status.user.screen_name, status.text, '\n'
    print status.user
    webbrowser.open(status.user.profile_image_url)

#print tweets
