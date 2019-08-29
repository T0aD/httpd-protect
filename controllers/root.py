
from basehandler import BaseHandler
import time, json, os
import iptables

class Controller(BaseHandler):

    def get(self, param=False):
        rv = iptables.whitelist(self.params, self.request.remote_ip)
        s = ""
        if not rv:
            s = " already"
        self.write(json.dumps({__file__: 'remote address %s%s whitelisted' % (self.request.remote_ip, s)}) + "\n")

