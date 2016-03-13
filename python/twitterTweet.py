# encoding utf-8
# https://gist.github.com/davej/113241
# http://www.ankitpanda.com/tweeting-with-python/

"""
Author:         David Gabanic
Description:    This script allows the user to tweet from the command line.

"""

import tweepy
import sys
import time
import threading

import twitterLogin

#TODO
# Implement 0-140 character check

# Tweets the time every minute
def send_scheduled_tweet():
    api.update_status(time.ctime())
    print("Tweet sent by @%s" % api.me().screen_name)
    threading.Timer(60, send_tweet).start()

# Tweets user input from command line
def send_tweet(tweet):
    api.update_status(tweet)
    print("Tweet sent by @%s" % api.me().screen_name)

if __name__ == "__main__":
    api = twitterLogin.oauth_login(twitterLogin.CONSUMER_KEY, twitterLogin.CONSUMER_SECRET)
    print ("Authenticated as @%s" % api.me().screen_name)

    send_tweet(sys.argv[1])
