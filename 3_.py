#!/usr/bin/env python
# -*- coding: utf-8 -*-
### author: rain ###

import urllib
import re

url = "http://www.pythonchallenge.com/pc/def/equality.html"
page = urllib.urlopen(url)
check = re.compile('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]')
text = page.read()
start = text.find(r'kAewtloYgcFQaJ')
key = "".join(check.findall(text[start:]))
print key,

