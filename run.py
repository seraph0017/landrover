#!/usr/bin/env python
#encoding:utf-8

from src.crawl import Crawl
from src.excel import Excel
from src import app

ids = [
        '805722326566'
        ]

def main():
    c = Crawl()
    c.run(ids)


def t():
    e = Excel(u'/Users/max/Downloads/2016年1月路虎对账单——NSC部分.xlsx')
    c = Crawl()
    for i in e.test():
        c.run(i)


def w():
    app.run(debug=True)



def create_db():
    from src.db import db
    db.create_all()


if __name__ == "__main__":
    #    main()
    #t()
    w()
    #create_db()
