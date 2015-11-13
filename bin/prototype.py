# -*- coding: utf-8 -*-
# Prototype for Termblr
# https://github.com/dianakhuang/pytumblr/tree/diana/python-3-support
from pytumblr import TumblrRestClient
import objectpath


client = TumblrRestClient(
    consumer_key='iWpkjxQeBaFBpIvHTB0RbP7G5ozicNZ5FQtiMkkoKFkiJ4Cfjb',
    consumer_secret='JfmKt6EJWOPdNs155kBrVC7AC8YO3V9RVJt73PcuU85E7buGsq',
    oauth_token='ZoegVG4B9pTAFm3lI86bSueW8KVlr0PKOkxNsh4CqmwIMnLRcE',
    oauth_secret='AkuR2qM8QNvEm62dQ8JbldxYicQJMvpxdOhfBQPALgsBWLrc7G',
)

user_info = client.info()
print("--- Welcome to the Termblr prototype. ---\n")
print("-"*15, "\nStart using the `client` object\n", "\n", "username:", user_info['user']['name'], "\n", "url:", user_info['user']['blogs'][0]['url'])
