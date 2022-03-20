import sys
import socketserver
from http.server import SimpleHTTPRequestHandler

class JsonpHTTPRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self): 
        # Include additional response headers here. CORS for example:       
        self.send_header('Access-Control-Allow-Origin', '*')
        #self.send_header('Content-Type', 'application/json')    
        SimpleHTTPRequestHandler.end_headers(self)
    
    def do_OPTIONS(self):
        self.send_response(200)
    
    
    
if __name__ == '__main__':
    PORT = 8000
    with socketserver.TCPServer(("localhost", PORT), JsonpHTTPRequestHandler) as httpd:
        print("Listening on port {}. Press Ctrl+C to stop.".format(PORT))
        httpd.serve_forever()