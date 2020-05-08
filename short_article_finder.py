#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telegram_util import log_on_fail
import time
import cached_url
from bs4 import BeautifulSoup

with open('channels.txt') as f:
	pool = f.read().split()
pool = [x.strip() for x in pool]
pool = [x for x in pool if x]

def getSoup(name):
    return BeautifulSoup(cached_url.get('https://telete.in/s/' + name), 'html.parser')

def getMessages():
    messages = {}
    for name in pool:
        soup = getSoup(name)
        for msg in soup.find_all('div', class_='tgme_widget_message'):
            msg = Message(msg)
            if msg.getTitle():
                messages[msg.getID()] = msg
    return messages

soup = BeautifulSoup(cached_url.get(LINK_PREFIX + source), 'html.parser')
	name = soup.find('meta', {'property': 'og:title'})['content']
	links = {}
	for item in soup.find_all('a', class_='tgme_widget_message_link_preview'):
		if 'telegra.ph' not in item['href']:
			continue
		title = item.find('div', class_='link_preview_title').text
		links[item['href']] = title