#!/usr/bin/env python
#encoding:utf-8
import os


POST_URL = 'http://trace.yto.net.cn:8022/TraceSimple.aspx'


HEADERS = {
        'Origin':'http://www.yto.net.cn',
        'Referer':'http://www.yto.net.cn/gw/service/Shipmenttracking.html',
        'Upgrade-Insecure-Requests':'1',
        }


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

CELERY_BROKER_URL               = 'redis://localhost:6379/1'
CELERY_RESULT_BACKEND           = 'redis://localhost:6379/2'
CELERY_IMPORTS                  = ('src.tasks',)

CELERY_DEFAULT_QUEUE            = "default"


UPLOAD_FOLDER = os.path.join(BASE_DIR, 'src/uploads')
DB_URI = 'mysql://root:1q2w3e4r@127.0.0.1/landrover'

