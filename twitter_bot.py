# %%
import tweepy
import os
import time
import randfacts
import setup
import bp_sql as bp
import sys

# %%
bp.log_errors('brett.passini@gmail.com','twitterbot')

# %%
tim = bp.timer('the timer')

# %%
consumer_api_key = setup.consumer_api_key
consumer_api_secret_key = setup.consumer_api_secret_key

access_token = setup.access_token
access_token_secret = setup.access_token_secret

twt_lim = 280

# %%
def tweet(twt_str):
    client = tweepy.Client(access_token=access_token, access_token_secret=access_token_secret, consumer_key=consumer_api_key, consumer_secret=consumer_api_secret_key)
    response = client.create_tweet(text=twt_str)


def get_fact():
    return randfacts.get_fact()

# %%
a = time.time()

fact_str = get_fact()

while len(fact_str) > twt_lim and (time.time()-a)<120:
    fact_str = get_fact()
else:
    tweet(fact_str)

# %%
tim.stop()

# %%



