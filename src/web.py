#!/usr/bin/env python
#encoding:utf-8

from os.path import join
from flask import render_template, request, redirect, url_for
from src import app
from src.tasks import download
from src.db import Record



@app.route('/', methods=['GET','POST'])
def index_handler():
    if request.method == 'POST':
        fi = request.files['excel']
        if fi:
            fi.save(join(app.config['UPLOAD_FOLDER'],fi.filename).encode('utf-8'))
            download.apply_async(args=(fi.filename,))
        return redirect(url_for('index_handler'))
    rs = Record.query.order_by(Record.insert_time.desc()).limit(10).all()
    return render_template('__base.html', rs=rs)





