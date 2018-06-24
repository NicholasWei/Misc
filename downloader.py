#!/usr/bin/env python3.6

import urllib.request
import ssl

prefix = 'https://vod.mudu.tv/watch/2018-06-23/%s'

file = open('todo', 'r')
ssl._create_default_https_context = ssl._create_unverified_context
for line in file:
    todownload = prefix % line
    urllib.request.urlretrieve(todownload, line)

file.close()

