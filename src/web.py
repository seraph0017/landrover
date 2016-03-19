#!/usr/bin/env python
#encoding:utf-8

from os.path import join
from flask import render_template, request, redirect, url_for, make_response
from src import app
from src.tasks import download
from src.db import Record
from functools import wraps
from settings import PWD



def login_required(func):
    @wraps(func)
    def _(*args, **kw):
        pwd = request.cookies.get('pwd')
        if pwd == PWD:
            return func(*args, **kw)
        return redirect(url_for('login_handler'))
    return _











@app.route('/', methods=['GET','POST'])
@login_required
def index_handler():
    print dir(request)
    print request.cookies
    if request.method == 'POST':
        fi = request.files['excel']
        if fi:
            fi.save(join(app.config['UPLOAD_FOLDER'],fi.filename).encode('utf-8'))
            download.apply_async(args=(fi.filename,))
        return redirect(url_for('index_handler'))
    rs = Record.query.order_by(Record.insert_time.desc()).limit(10).all()
    return render_template('__base.html', rs=rs)




@app.route('/login', methods=['GET','POST'])
def login_handler():
    if request.method == 'POST':
        pwd = request.form.get('password')
        print pwd
        if pwd == PWD:
            resp = make_response(redirect(url_for('index_handler')))
            resp.set_cookie('pwd', PWD)
            return resp
        return redirect(url_for('login_handler'))
    return render_template('login.html')

