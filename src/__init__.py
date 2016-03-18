#!/usr/bin/env python
#encoding:utf-8

from os.path import join
from flask import Flask
from settings import BASE_DIR, UPLOAD_FOLDER, DB_URI


app = Flask(__name__)
app.template_folder = join(BASE_DIR, 'src', 'templates')
app.static_folder = join(BASE_DIR, 'src', 'static')

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.template_filter('upurl')
def upurl(s):
    return u'uploads{}'.format(s.split('uploads')[-1])

@app.template_filter('upname')
def upname(s):
    return s.split('uploads/')[-1]

@app.template_filter('dwurl')
def dwurl(s):
    return u'downloads{}'.format(s.split('downloads')[-1])

@app.template_filter('dwname')
def dwname(s):
    return s.split('downloads/')[-1]


from src.web import *
