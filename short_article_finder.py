#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import cached_url
from bs4 import BeautifulSoup
from preview import getNextPos, getLinks
from pool import Pool
from checker import check

pool = Pool()

while pool.pool:
	for name, pos in [x, pool.pool[x] for x in pool.pool]:
		for link in getLinks(name, pos):
			if check(link):
				print(link)
		next_pos = getNextPos(name, pos)
		pool.update(name, next_pos)