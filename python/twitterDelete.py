# encoding utf-8
# http://www.ireckon.net/2015/03/delete-old-tweets-selectively-using-python-and-tweepy
# http://miguelmalvarez.com/2015/03/03/download-the-pictures-from-a-twitter-feed-using-python/

"""
Author:         David Gabanic
Description:    This script will delete all tweets after a specific number of days
                in order to avoid future embarassing moments courtesy of Timehop.
"""

import tweepy
import sys
import csv
import wget

import twitterLogin

from datetime import datetime, timedelta

# Options
delete_tweets = True
verbose = True
test_mode = True

# This number indicates how many days worth of tweets you'd like to keep
older_than_these_days = 14

# Sets cutoff date; uses UTC to match Twitter
cutoff_date = datetime.utcnow() - timedelta(days = older_than_these_days)

# Initialize media variable
media_files = set()

def tweet_delete():
    csvFile = open('tweetArchive.csv', 'a', encoding='utf-8')
    csvWriter = csv.writer(csvFile)

    if delete_tweets:
        # Get all tweets
        print ("Retrieving tweets from timeline")
        timeline = tweepy.Cursor(api.user_timeline).items()
        deleted_count = 0
        ignored_count = 0

        for tweet in timeline:
            # Checks if there is media associated with the tweet
            media = tweet.entities.get('media', [])
            if(len(media) > 0):
                media_files.add(media[0]['media_url'])
                #wget.download(media_files)

            # where tweets are not in "saved" list and older than cutoff date
            if tweet.id and tweet.created_at < cutoff_date:
                csvWriter.writerow([tweet.id, tweet.created_at, tweet.text])
                if verbose:
                    print ("Deleting %d: [%s] %s" % (tweet.id, tweet.created_at, tweet.text))
                if not test_mode:
                    api.destroy_status(tweet.id)
                deleted_count += 1
            else:
                ignored_count += 1

        print ("Deleted %d tweets, ignored %d" % (deleted_count, ignored_count))
    else:
        print ("No tweets were deleted")

    csvFile.close()

if __name__ == "__main__":
    api = twitterLogin.oauth_login(twitterLogin.CONSUMER_KEY, twitterLogin.CONSUMER_SECRET)
    print ("Authenticated as @%s" % api.me().screen_name)

    tweet_delete()
