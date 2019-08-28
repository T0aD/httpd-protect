#! /usr/bin/python -u
# -*- coding: utf-8 -*- 

from tornado.web import Application, RequestHandler, StaticFileHandler
from tornado.ioloop import IOLoop

import time, json, os
import logging
import tornado.log
from tornado.log import access_log, app_log, gen_log


def make_app(params):
  ################################################################## ROUTES
  parameters = dict(params=params)

  from controllers import auth
  
  urls = [
    ("/", auth.Controller, parameters),
  ]
  settings = {}
  return Application(urls, **settings)


################################################################# ENTRYPOINT

def main(params):
  logging.getLogger('tornado.access').setLevel(logging.INFO)
  #logging.getLogger("tornado.application").setLevel(logging.INFO)

  from tornado.log import app_log
  #print app_log, app_log.setLevel, app_log.info
  app_log.setLevel(logging.INFO)

  app = make_app(params)
  app.listen(params.port)
  print 'started httpd on :%d' % params.port
  IOLoop.instance().start()


if __name__ == '__main__':
  import argparse
  parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

  g = parser.add_argument_group("Server")
  g.add_argument('--port', '-p', type=int, default=3000,        help="port to bind httpd server to")

  g = parser.add_argument_group("Firewall")
  g.add_argument('--username', type=str, default="admin",       help="username used to whitelist")
  g.add_argument('--password', type=str, default="adminpwd",    help="password to whitelist")
  g.add_argument('--protected-port', type=int, nargs='*', default=[9200],    help="port to protect")
  g.add_argument('--chain-name', type=str, default="protector", help="default name of the chain to use to protect targetted ports")

  #parser.add_argument('--log-level', default=0)
  #parser.add_argument('--debug', default=False, action='store_true')
  #parser.add_argument('argv', nargs='*')
  params = parser.parse_args()

  print params
  main(params)

