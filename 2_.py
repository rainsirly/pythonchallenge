#!/usr/bin/env python
# -*- coding: utf-8 -*-
### author: rain ###

import urllib
import re

url = "http://www.pythonchallenge.com/pc/def/ocr.html"
page = urllib.urlopen(url)
check = re.compile('[a-zA-Z]+')
text = page.read()
start = text.find(r'%%$@_$^__#)^)&!_+]!*@&^}')
key = "".join(check.findall(text[start:]))
print key,
       
