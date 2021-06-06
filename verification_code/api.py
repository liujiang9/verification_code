#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/6 13:29
# @Author  : LiuJiang
# @File    : api.py
# @Software: PyCharm
import re

from flask import Flask, g, request
from db import Reids_Client

__all_ = ['testcase']

app = Flask(__name__)


def get_conn():
    if not hasattr(g, 'redis_client'):
        g.redis_client = Reids_Client()
    return g.redis_client


@app.route('/get')
def get():
    return re.findall('验证码(.*?)，请', get_conn().pop())[0]


@app.route('/message', methods=['POST'])
def index():
    r = request.args.get('yz')
    if '阿里巴巴' in r:
        get_conn().put(r)
        return r
    else:
        return '不是阿里短信'


@app.route('/count')
def count():
    return str(get_conn().queue_len)
