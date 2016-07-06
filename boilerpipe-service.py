#!/usr/bin/env python

import requests
import urllib
import time

url = 'http://www.techtimes.com/articles/167409/20160629/huawei-will-debut-new-smartphones-on-september-1-heres-what-to-expect.htm'

url =  urllib.quote(url, '')

url = 'https://boilerpipe-web.appspot.com/extract?url=' + url + '&extractor=ArticleExtractor&output=text&extractImages=&token='

print url

while True:
	r = requests.get(url, verify=False)
	if r.status_code == 200:
		print r.text
		break
	else:
		time.sleep(4)


