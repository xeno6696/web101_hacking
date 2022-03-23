import sys
import socketserver
import pdb
from http.server import SimpleHTTPRequestHandler

class JsonpHTTPRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self): 
        # Include additional response headers here. CORS for example:       
        self.send_header('Access-Control-Allow-Origin', 'https://fiddle.jshell.net')
        self.send_header('Access-Control-Allow-Headers','*')
        #self.send_header('Content-Type', 'application/json')    
        SimpleHTTPRequestHandler.end_headers(self)
    
    def do_OPTIONS(self):
        #print(type(self))
        #pdb.set_trace()
        print(self.headers)
        self.send_response(200)
        self.send_header('Access-Control-Allow-Methods', 'GET')
        self.send_header('Origin','fiddle.jshell.net')
        self.end_headers()
        return
        
        
    
    
    
if __name__ == '__main__':
    PORT = 8000
    with socketserver.TCPServer(("localhost", PORT), JsonpHTTPRequestHandler) as httpd:
        print("Listening on port {}. Press Ctrl+C to stop.".format(PORT))
        httpd.serve_forever()