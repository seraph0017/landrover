#!/usr/bin/env python
#encoding:utf-8

import xlrd
import xlwt

import sys
reload(sys)
sys.setdefaultencoding('utf-8')



class Excel(object):

    def __init__(self, fpath):
        self._data = xlrd.open_workbook(fpath.encode('utf-8'))
        self._sheet = self._data.sheets()[0]


    def test(self):
        nrows = self._sheet.nrows
        r_list = []
        for i in range(3, nrows):
            r_list.append(self._sheet.row_values(i)[5])
            if len(r_list) >= 10 or (nrows - i) < 10:
                yield r_list
                r_list = []


class Wexcel(object):

    def __init__(self, fpath):
        self._data = xlwt.Workbook()
        self._fpath = fpath
        self._table = self._data.add_sheet('landrover',cell_overwrite_ok=True)


    def write(self, x, y, item):
        self._table.write(x,y,item)


    def save(self):
        self._data.save(self._fpath.encode('utf-8'))














