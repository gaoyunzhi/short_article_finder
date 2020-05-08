import readee
import cached_url
from telegram_util import cnWordCount

def check(link):
	content = cached_url.get(link, force_cache = True)
	soup = readee.export(link, content = content)
	if 200 < cnWordCount(soup.text) < 2500:
		return True
	return False
