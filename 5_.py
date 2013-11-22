#!/usr/bin/env python
# -*- coding: utf-8 -*-
### author: rain ###
### learned python pickle model from other's advice

import urllib
import pickle

#the first vision
url = r"http://www.pythonchallenge.com/pc/def/banner.p"
page = urllib.urlopen(url)
data = pickle.load(page)
for ele in data:
    key = ""
    for char in ele:
        key += "".join(char[0]*char[1])
    print key

#the update vision
for ele in data:
    key = "".join(map(lambda p: p[0]*p[1], ele))
    print key
