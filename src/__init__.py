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



from src.web import *
