#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Torrez, Milton N.

import requests
import json

#  URLS
penRss = "https://codepen.io/torrezmn/public/feed/"
rss2jsonApi = "https://api.rss2json.com/v1/api.json?rss_url=" + penRss


req = requests.get(rss2jsonApi)

data = json.loads(req.text)


with open("codepens.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
