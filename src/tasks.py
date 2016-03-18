#!/usr/bin/env python
#encoding:utf-8


from src.crawl import Crawl
from src.excel import Excel, Wexcel
from settings import BASE_DIR
from os.path import join
from src.db import Record, db

from celery import Celery, platforms
from celery.utils.log import get_task_logger
from settings import (CELERY_BROKER_URL, 
        CELERY_RESULT_BACKEND, 
        CELERY_IMPORTS,
        CELERY_DEFAULT_QUEUE)

logger = get_task_logger(__name__)
platforms.C_FORCE_ROOT = True
celery  = Celery('james', 
        broker=CELERY_BROKER_URL, 
        backend=CELERY_RESULT_BACKEND)

celery.conf['CELERY_IMPORTS'] = CELERY_IMPORTS
celery.conf['CELERY_DEFAULT_QUEUE'] = CELERY_DEFAULT_QUEUE



@celery.task(bind=True,default_retry_delay=60,max_retries=5)
def download(self, fname):
    upload_fp = join(BASE_DIR, u'src/uploads', fname)
    download_fp = join(BASE_DIR, u'src/downloads', u'{}-订单状态.xls'.format(fname.rsplit('.',-1)[0]))
    e = Excel(upload_fp)
    w = Wexcel(download_fp)
    c = Crawl()
    a = 0
    r = Record(
            fname = fname,
            upload_fp = upload_fp,
            download_fp = download_fp,
            status = False)
    db.session.add(r)
    db.session.commit()
    for i in e.test():
        for code, status in c.run(i):
            logger.info(u"{} ==>>> {}".format(code, status))
            w.write(a, 0, code)
            w.write(a, 1, status)
            a += 1
    w.save()
    r.status = True
    db.session.add(r)
    db.session.commit()


