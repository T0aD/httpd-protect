import tornado
import json
import base64

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
        self.check_authenticated()

    def options(self, param=False):
        self.set_header("Allow", "GET,HEAD,PUT,POST,DELETE,OPTIONS")
        self.set_status(200)

    def request_auth(self):
        self.set_status(401)
        self.set_header('WWW-Authenticate', 'Basic realm=%s' % self.params.realm)
        self.finish()
        return False

    def check_authenticated(self):
        if not "Authorization" in self.request.headers:
            return self.request_auth()
        
        auth_decoded = base64.decodestring(self.request.headers["Authorization"][6:])
        username, password = auth_decoded.split(':', 2)

        if self.params.username != username:
            return self.request_auth()
        if self.params.password != password:
            return self.request_auth()

        self.username, self.password = username, password

        return True



