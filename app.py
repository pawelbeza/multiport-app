import threading
import argparse
from http.server import HTTPServer, SimpleHTTPRequestHandler
from http import HTTPStatus

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        self.wfile.write(b'Hello world')

def start_httpd(port: int):
    server_address = ('', port)
    httpd = HTTPServer(server_address, Handler)
    httpd.serve_forever()


if __name__=='__main__':
    parser = argparse.ArgumentParser(
        prog='multiport app',
        description='A test hello world multiport app. You know, for kids."',
    )

    parser.add_argument("-p", "--ports", type=int, nargs='+', required=True)
    args = parser.parse_args()

    for port in args.ports:
        threading.Thread(target=start_httpd, args=[port]).start()
