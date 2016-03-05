# encoding utf-8

"""
Author:         David Gabanic
Description:    This program will delete all tweets after a specific number of days
                in order to avoid future embarassing moments courtesy of Timehop.
"""

import tweepy
import sys

# Credentials for dummy account
CONSUMER_KEY = "vSdsm3c1GGNNsJhtj5oeSp3nY"
CONSUMER_SECRET = "F7F3kVJMVIUoOIkOvpTrGR7TC2d6ZWUt8DtIFfLpOBbbeM1xj0"
ACCESS_TOKEN = "4896423785-n9MTScfVR42W32kIu4zByNCaVe5fzq1FEZlFz5G"
ACCESS_TOKEN_SECRET = "5ndwLxhDEamVPMY7Gn3QIM8L6x2rAGvfoN5OsAGHCtlMW"

def oauth_login(key, secret):
    #Authentication via Twitter

    auth = tweepy.OAuthHandler(key, secret)
    #auth_url = auth.get_authorization_url()

    #verify = input("Authenticate at %s and then enter your verification code here: " % auth_url)
    #auth.get_access_token(verify)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    return tweepy.API(auth)

if __name__ == "__main__":
    api = oauth_login(CONSUMER_KEY, CONSUMER_SECRET)
    print ("Authenticated as @%s" % api.me().screen_name)
    api.update_status(sys.argv[1])
