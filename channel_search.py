#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from preview import getNextPos, getLinks, getSoup
from pool import Pool
import yaml
import os
from telegram_util import matchKey

def search(keywords):
	pool = Pool()
	while pool.pool:
		for name, pos in pool.items():
			if matchKey(getSoup(name, pos).text, keywords):
				print(getRootUrl(name, post))
			next_pos = getNextPos(name, pos)
			pool.update(name, next_pos)

if __name__ == "__main__":
	search(['方言', '家乡', '传统'])