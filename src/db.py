#!/usr/bin/env python
#encoding:utf-8


from datetime import datetime
from src import app 
from flask.ext.sqlalchemy import SQLAlchemy


db = SQLAlchemy(app)


class Record(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(255))
    upload_fp = db.Column(db.String(255))
    download_fp = db.Column(db.String(255))
    status = db.Column(db.Boolean)
    insert_time = db.Column(db.DateTime, default=datetime.now)


