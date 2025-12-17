from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

WEBROOT = "/var/www/certbot"
PORT = 80

os.makedirs(WEBROOT, exist_ok=True)
os.chdir(WEBROOT)

httpd = HTTPServer(("0.0.0.0", PORT), SimpleHTTPRequestHandler)
print(f"Serving {WEBROOT} on port {PORT}")
httpd.serve_forever()
