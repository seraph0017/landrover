#!/usr/bin/env python
#encoding:utf-8

import requests
from bs4 import BeautifulSoup

from settings import HEADERS, POST_URL


class Crawl(object):


    def __init__(self):
        self._req = requests.Session()
        self._req.headers = HEADERS


    def run(self, ids):
        data = {
                'waybillNo': '/'.join(ids),
                'validateCode': '',
                }
        res = self._req.post(POST_URL,data = data)
        html = BeautifulSoup(res.content)
        trace_boxs = html.select('div.trace-box')
        for box in trace_boxs:
            code = box.select('.box-hd strong')[0].text.strip() 
            status = box.select('td')[-1].text.strip().replace(u'感谢使用圆通速递，期待再次为您服务', '')
            yield code, status
