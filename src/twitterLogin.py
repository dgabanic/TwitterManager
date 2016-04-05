# encoding utf-8
# https://github.com/olivierthereaux/oldtweets/blob/master/oldtweets.py

"""
Author:         David Gabanic
Description:    This script authenticates the user to access the Twitter account.

NOTE:           THIS IS THE LIVE FILE THAT LOGS INTO @David_Gabanic

"""

import tweepy
import sys

import credentials

def oauth_login(key, secret):
    #Authentication via Twitter

    auth = tweepy.OAuthHandler(key, secret)
    #auth_url = auth.get_authorization_url()

    #verify = input("Authenticate at %s and then enter your verification code here: " % auth_url)
    #auth.get_access_token(verify)
    auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_TOKEN_SECRET)

    return tweepy.API(auth)
