import tweepy

CONSUMER_KEY = 'p0eq8NMKUmBQGJDugMNpW1hb8'
CONSUMER_SECRET = 'eKgaNjZh3kUCSB8VwAItsYGpg3eZ1rUNY21PjvYihvWwzPpRTG'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.secure = True
auth_url = auth.get_authorization_url()
print 'Please authorize: ' + auth_url
verifier = raw_input('PIN: ').strip()
auth.get_access_token(verifier)
print "ACCESS_KEY = '%s'" % auth.access_token.key
print "ACCESS_SECRET = '%s'" % auth.access_token.secret
