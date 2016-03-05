# encoding utf-8

"""
Author:         David Gabanic
Description:    This script allows the user to tweet from the command line.

"""

import tweepy
import sys

import twitterLogin

if __name__ == "__main__":
    api = twitterLogin.oauth_login(twitterLogin.CONSUMER_KEY, twitterLogin.CONSUMER_SECRET)
    print ("Authenticated as @%s" % api.me().screen_name)

    api.update_status(sys.argv[1])
