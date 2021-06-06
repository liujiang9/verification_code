#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/6 13:30
# @Author  : LiuJiang
# @File    : db.py
# @Software: PyCharm
import redis
from settings import HOST, PASSWORD, PORT, PROXY_NAME


class Reids_Client(object):
    def __init__(self, host=HOST, port=PORT, password=PASSWORD):
        if password:
            self.__conn = redis.Redis(host=host, port=port, password=password)
        else:
            self.__conn = redis.Redis(host=host, port=port)

    def put(self, proxy):
        self.__conn.rpush(PROXY_NAME, proxy)

    def pop(self):
        return self.__conn.lpop(PROXY_NAME).decode('utf-8')

    def get(self, count=1):
        proxies = self.__conn.lrange(PROXY_NAME, 0, count - 1)
        self.__conn.ltrim(PROXY_NAME, count, -1)
        return proxies

    @property
    def queue_len(self):
        return self.__conn.llen(PROXY_NAME)

    def flush(self):
        self.__conn.flushdb()
