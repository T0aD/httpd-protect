
from basehandler import BaseHandler
import time, json, os
import iptables

class Controller(BaseHandler):

    def get(self, param=False):
        self.write(json.dumps({'message': 'this is %s' % __file__}) + "\n")

        iptables.down(self.params)
        iptables.up(self.params)
