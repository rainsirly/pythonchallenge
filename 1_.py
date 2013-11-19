#!/usr/bin/env python
# -*- coding: utf-8 -*-
### author: rain ###

# this is my way to solve the problem
hints = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

dic = {"y" : "a",
       "z" : "b",
       "Y" : "A",
       "Z" : "B"}
for word in hints.split():
    w = ""
    for char in word:
        if char.isalpha():
            if char in dic.keys():
                char = dic[char]
            else:
                char = chr(ord(char)+2)
        w += char
    print w,
print

# and the hints way under
import string

table = string.maketrans('abcdefghijklmnopqrstuvwxyz','cdefghijklmnopqrstuvwxyzab')
print hints.translate(table)

