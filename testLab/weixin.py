__author__ = 'stone'
#encoding:utf-8
#File:order.py

import web
from web.contrib.template import render_mako

import traceback
from logHelper import getLogger

import re
import base64
import json
import urlparse

web.config.debug = False

urls = (
        '/','index',
        )

app = web.application(urls,globals(),autoreload=True)
session = web.session.Session(app,web.session.DiskStore('sessions'),
    initializer={'session_grpid':'','session_usrid':'','session_loginned':'','session_pwd':''})

def session_hook():
    web.ctx.session = session

app.add_processor(web.loadhook(session_hook))

class index:
    def POST(self):
        try:
            logger = getLogger()
            logger.debug("start Index Page POST response")

            #TODO: 要加入微信的加密/校验流程.

        except :
            logger.error("exception occur, see the traceback.log")
            #异常写入日志文件.
            f = open('traceback.txt','a')
            traceback.print_exc()
            traceback.print_exc(file = f)
            f.flush()
            f.close()
        else:
            pass
        finally:
            pass

    def GET(self):
        try:
            logger = getLogger()
            logger.debug("start Index Page GET response")

            parsed_url = urlparse.urlparse(web.ctx.fullpath)
            query_url = parsed_url.query

            if (query_url != ''):
                query_dict = dict(urlparse.parse_qsl(query_url))

                echostr = query_dict['echostr']

            else:
                pass

            return echostr

        except :
            logger.error("exception occur, see the traceback.log")
            #异常写入日志文件.
            f = open('traceback.txt','a')
            traceback.print_exc()
            traceback.print_exc(file = f)
            f.flush()
            f.close()
        else:
            pass
        finally:
            pass

if __name__ == "__main__":
    app.run()

