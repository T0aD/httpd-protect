#! /usr/bin/python -u
# -*- coding: utf-8 -*- 

from tornado.web import Application, RequestHandler, StaticFileHandler
from tornado.ioloop import IOLoop

import time, json, os
import logging
import tornado.log
from tornado.log import access_log, app_log, gen_log
import iptables

def make_app(params):
  ################################################################## ROUTES
  parameters = dict(params=params)

  from controllers import root
  
  urls = [
    ("/", root.Controller, parameters),
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
  try:
    iptables.up(params)
  except Exception as e:
    print e.message
    exit(1)
  try:
    IOLoop.instance().start()
  except:
    iptables.down(params)
    raise


if __name__ == '__main__':
  import argparse
  parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

  g = parser.add_argument_group("Server")
  g.add_argument('--port', '-p', type=int, default=3003,        help="port to bind httpd server to")

  g = parser.add_argument_group("Basic auth")
  g.add_argument('--username', type=str, default="admin",       help="username used to whitelist")
  g.add_argument('--password', type=str, default="adminpwd",    help="password to whitelist")
  g.add_argument('--realm', type=str, default="httpd-protect",    help="name of the realm to display")

  g = parser.add_argument_group("Iptables")
  g.add_argument('--protected-port', type=int, nargs='*', default=[9200,9300],    help="port to protect")
  g.add_argument('--chain-name', type=str, default="httpd-protected", help="default name of the chain to use to protect targetted ports")
  g.add_argument('--allow', type=str, nargs='*', default=["172/8"],    help="list of addresses to whitelist from the start")

  #parser.add_argument('--log-level', default=0)
  #parser.add_argument('--debug', default=False, action='store_true')
  #parser.add_argument('argv', nargs='*')
  params = parser.parse_args()

  print params
  main(params)

