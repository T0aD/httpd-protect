
from basehandler import BaseHandler
import time, json, os

class Controller(BaseHandler):

    def post(self, param=False):
        self.write(json.dumps({'message': 'this is %s' % __file__}) + "\n")

    def get(self, param=False):
        self.write(json.dumps({'message': 'this is %s' % __file__}) + "\n")
