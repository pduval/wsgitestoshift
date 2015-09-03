# Main entry point of the Main WSGI application.
# Should be auto-detected by Openshift Python STI

class TestWsgiApp(object):
    def __init__(self, environment):
        self.environment = environment
        
    def __call__(self, env, start_response):

        lines = [
            """<!DOCTYPE html>
<html>
   <head><title>Openshift WSGI Info</title></head>
</html>
<body>
  <table style="width:100%">
    <thead><tr><th colspan="2">Main Environment</th></tr>
           <tr><th>Key</th><th>Value</th></tr>
    </thead>
    <tbody>
"""
]
        for k,v in self.environment.iteritems():
            lines.append("<tr><td>{0}</td><td>{1}</td></tr>\n".format(k,v))
        lines.append("</tbody></table>")
        lines.append("""
  <table style="width:100%">
    <thead><tr><th colspan="2">Request Environment</th></tr>
           <tr><th>Key</th><th>Value</th></tr>
    </thead>
    <tbody>
        
            """)
        for k,v in env.iteritems():
            lines.append("<tr><td>{0}</td><td>{1}</td></tr>\n".format(k,v))
        lines.append("</tbody></table>")

        lines.append("</body></html>")
        start_response('200 OK', [])
        return lines

import os
application = TestWsgiApp(os.environ)
