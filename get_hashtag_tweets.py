#! /usr/bin/env python


import sys
import tweepy
#import webbrowser
from PIL import Image, ImageFont, ImageDraw
import urllib2
import io


def main():
    CONSUMER_KEY = 'p0eq8NMKUmBQGJDugMNpW1hb8'
    CONSUMER_SECRET = 'eKgaNjZh3kUCSB8VwAItsYGpg3eZ1rUNY21PjvYihvWwzPpRTG'
    ACCESS_KEY = '40087586-E2lSs4DOYf7yzFFlB66glfOdKG1i71CBgnXY6BCDS'
    ACCESS_SECRET = 'hjHEUP54AV2sEAS9xrxSbR9hm0Z34ClNC6DQyXzP9JY48'

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.secure = True
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    tweets = []

    #tag = raw_input('Hashtag: ').strip()
    tag = 'kelchwedding2014'

    for status in tweepy.Cursor(api.search, q=tag, locale='en',).items():
        print status.user.name, '@'+status.user.screen_name, status.text, '\n'
        make_image(status.user.profile_image_url, status.text, status.user.screen_name, status.user.name)
        #print status.user
        #webbrowser.open(status.user.profile_image_url)

        #print tweets

def make_image(url, txt, handle, name):
    psize = 75
    background = Image.new( 'RGB', (500,250), 'white') # create a new white image

    path = io.BytesIO(urllib2.urlopen(url).read())
    profile_img = Image.open(path)
    profile_img = profile_img.resize((psize, psize))
    background.paste(profile_img, (10, 10))

    draw = ImageDraw.Draw(background)
    font = ImageFont.truetype('BorisBlackBloxx.ttf', 22)
    #font = ImageFont.truetype('/System/Library/Fonts/Helvetica.dfont', 22)
    draw.text((10, psize+20), txt, (0,0,0),font=font)
    draw.text((psize+20, 15), name, (0,0,0),font=font)
    draw.text((psize+20, 45), '@'+handle, (0,0,0),font=font)
    draw = ImageDraw.Draw(background)

    background.show()
    #profile_img.show()

if __name__ == '__main__':
    main()
