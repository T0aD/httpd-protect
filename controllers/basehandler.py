import tornado
import json

class BaseHandler(tornado.web.RequestHandler):
    def _request_summary(self):
        try:
            summary = "%s %s (%s)" % (self.request.method, self.request.uri, self.request.remote_ip)
            return summary
        except:
            print 'problem while creating summary with:'
        return self.request.method + " " + self.request.uri + \
            " (" + self.request.remote_ip + ") special"


    def initialize(self, params):
        self.params = params

    def set_default_headers(self):
        self.set_header('Server', 'httpd-protect/0.1')

    def prepare(self):
        if "X-Forwarded-For" in self.request.headers:
            remote_ip = self.request.headers["X-Forwarded-For"]
            self.request.remote_ip = remote_ip

    def options(self, param=False):
        self.set_header("Allow", "GET,HEAD,PUT,POST,DELETE,OPTIONS")
        self.set_status(200)
