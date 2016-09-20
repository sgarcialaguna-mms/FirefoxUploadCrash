# -*- coding: utf-8 -*-

import BaseHTTPServer
import time
import random

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    """
    For more information on CORS see:
    * https://developer.mozilla.org/en-US/docs/HTTP/Access_control_CORS
    * http://enable-cors.org/
    """
    def do_OPTIONS(self):
        self.send_response(200, "ok")
        # set CORS headers
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Headers', 'content-disposition')
        self.end_headers()

    def do_POST(self, *args, **kwargs):
        time.sleep(random.random() * 0.1)
        self.send_response(200)
        # set CORS headers
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Headers', 'content-disposition')
        self.end_headers()


def httpd():
    try:
        srvr = BaseHTTPServer.HTTPServer(('127.0.0.1', 8000), MyHandler)
        srvr.serve_forever()
    except KeyboardInterrupt:
        srvr.socket.close()


if __name__ == "__main__":
    httpd()
