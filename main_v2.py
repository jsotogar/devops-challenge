import http.server
import socketserver

PORT = 8888
API_KEY = '2f5ae96c-b558-4c7b-a590-a501ae1c3f6c'

class DevOpsHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        print(f"Received GET request for {self.path}")
        if self.path == '/devops':
            if self.headers.get('API-Key', '').lower() != API_KEY.lower():
                self.send_error(401, 'Unauthorized')
                return
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'DevOps handler test OK')
        else:
            self.send_error(404, 'File Not Found')
        

    def do_POST(self):
        print(f"Received POST request for {self.path}")
        if self.headers.get('API-Key', '').lower() != API_KEY.lower():
            self.send_error(401, 'Unauthorized')
            return
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length)
        response_message = b'Hello Juan Perez your message will be send'
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(response_message)

with socketserver.TCPServer(('', PORT), DevOpsHandler) as httpd:
    print('serving at port', PORT)
    httpd.serve_forever()
