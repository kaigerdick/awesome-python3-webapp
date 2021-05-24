#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'DK'

'''
async web application
'''

import logging; logging.basicConfig(level=logging.INFO)  #导入logging模块，设置日志basiConfig为INFO
import asyncio, os, json, time     #导入asyncio异步IO,os系统文件和目录操作，json轻量数据交换格式，time系统时间模块
from datetime import datetime     #导入datetime模块里的datetime函数，日期
from aiohttp import web           #导入aiohttp框架里的web函数

async def index(request):
    return web.Response(body=b'<h1>Awesome</h1>',content_type='text/html')
    #web.Response()有默认的status=200,headers=None,body=None,content_type=None,text=None设置

def init():
    app=web.Application()   #创建web服务器实例app
    app.add_routes([web.get('/',index)])
    logging.info('Server started at 127.0.0.1...') #日志info的输出格式
    web.run_app(app,host='127.0.0.1',port=8080)

init()
