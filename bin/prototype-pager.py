#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Prototype for Termblr
# https://github.com/dianakhuang/pytumblr/tree/diana/python-3-support
import sys
import os
sys.path.insert(0, '.')
MODULE_PATH = os.path.split(os.path.realpath(__file__))[0]

from pytumblr import TumblrRestClient
from objectpath import Tree


class Query(object):
    """
    Takes a stream of JSON.
    """
    def __init__(self, stream):
        self.tree = Tree(stream)
        self.execute = self.tree.execute
        self.post_queries = (lambda self=self: {v: "$.posts.{}".format(v) for v in self.execute("$.posts")[0].keys()})()

    def __repr__(self):
        return "<Query object>"


def show_dashboard():
    post =\
"""\
--------

Username: {blog_name}
Date: {date}
Post type: {type}

:: {title} ::
 {body}

Tags: {tags}
Notes: {note_count}
URL: {post_url}
"""
    for i in query.execute("$.posts"):
        print(post.format(**i))

client = TumblrRestClient(
    consumer_key='iWpkjxQeBaFBpIvHTB0RbP7G5ozicNZ5FQtiMkkoKFkiJ4Cfjb',
    consumer_secret='JfmKt6EJWOPdNs155kBrVC7AC8YO3V9RVJt73PcuU85E7buGsq',
    oauth_token='ZoegVG4B9pTAFm3lI86bSueW8KVlr0PKOkxNsh4CqmwIMnLRcE',
    oauth_secret='AkuR2qM8QNvEm62dQ8JbldxYicQJMvpxdOhfBQPALgsBWLrc7G',
)

dashboard = client.dashboard(type="text")
query = Query(dashboard)

user_info = client.info()
print("--- Welcome to the Termblr prototype. ---\n")
print("-"*15, "\nStart using the `client` object\n", "\n", "username:", user_info['user']['name'], "\n", "url:", user_info['user']['blogs'][0]['url'])

show_dashboard()
