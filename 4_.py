#!/usr/bin/env python
# -*- coding: utf-8 -*-
### author: rain ###

import urllib
import re

url_start = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=8022"
#the num(12345) will changed while the web visit running, and themilestone is 16044(need to
#divide it by two and keep going)
check = re.compile(r'([0-9]+)')
url_num = check.findall(url_start)[-1]
url_head = url_start.rsplit(url_num)[0]
while True:
    url = "%s%s" % (url_head, url_num)
    try:
        page = urllib.urlopen(url)
        print "visit page %s" % url
    except:
        print "cannt open page %s" % url
        break
    text = page.read()
    try:
        url_num = check.findall(text)[-1]
    except:
        print text
        break
