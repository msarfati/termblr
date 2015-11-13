#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pytumblr import TumblrRestClient
from objectpath import Tree
import urwid

client = TumblrRestClient(
    consumer_key='iWpkjxQeBaFBpIvHTB0RbP7G5ozicNZ5FQtiMkkoKFkiJ4Cfjb',
    consumer_secret='JfmKt6EJWOPdNs155kBrVC7AC8YO3V9RVJt73PcuU85E7buGsq',
    oauth_token='ZoegVG4B9pTAFm3lI86bSueW8KVlr0PKOkxNsh4CqmwIMnLRcE',
    oauth_secret='AkuR2qM8QNvEm62dQ8JbldxYicQJMvpxdOhfBQPALgsBWLrc7G',
)


def show_dashboard():
    tree = Tree(client.dashboard(type="text"))
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
    return post.format(tree.execute("$.posts")[0])

def scroll_up():
    txt.set_text("Scrolling up")


def scroll_down():
    txt.set_text("Scrolling down")


palette = [
    ('body','black','light gray', 'standout'),
    ('reverse','light gray','black'),
    ('header','white','dark red', 'bold'),
    ('important','dark blue','light gray',('standout','underline')),
    ('editfc','white', 'dark blue', 'bold'),
    ('editbx','light gray', 'dark blue'),
    ('editcp','black','light gray', 'standout'),
    ('bright','dark gray','light gray', ('bold','standout')),
    ('buttn','black','dark cyan'),
    ('buttnf','white','dark blue','bold'),
]


def show_key_or_exit(key):
    if key in ('f8'):
        raise urwid.ExitMainLoop()
    frame.footer = urwid.AttrWrap(urwid.Text(
        [u"Pressed: ", key.__repr__()]), 'header')

text_header = (u"Ƹ̵̡❀ Ｔｅｒｍｂｌｒ ❀̵̨̄Ʒ\n(F8 to quit)")

listbox_content =[
    urwid.Divider(),
    urwid.Text(u"This is a sample story", align='center'),
    urwid.Divider(),
]


header = urwid.AttrWrap(urwid.Text(text_header, align='center'), 'header')
listbox = urwid.ListBox(urwid.SimpleListWalker(listbox_content))
frame = urwid.Frame(urwid.AttrWrap(listbox, 'body'), header=header)

loop = urwid.MainLoop(
    widget=frame,
    palette=palette,
    screen=urwid.raw_display.Screen(),
    unhandled_input=show_key_or_exit,
)
loop.run()
