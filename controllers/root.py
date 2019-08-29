
from basehandler import BaseHandler
import time, json, os
import iptables

class Controller(BaseHandler):

    def get(self, param=False):
        iptables.whitelist(self.params, self.request.remote_ip)
        self.write(json.dumps({__file__: 'remote address %s whitelisted' % self.request.remote_ip}) + "\n")

