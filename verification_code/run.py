#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/6 13:32
# @Author  : LiuJiang
# @File    : run.py
# @Software: PyCharm

from api import app


def main():
    app.run(host='0.0.0.0',port=8801)


if __name__ == '__main__':
    main()
