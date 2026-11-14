"""
Birthday website server for Mehanaz Riya.

Put this file in the same folder as index.html and page2.html, then run:
    python server.py
It opens index.html (page 1) in your browser. Page 1 links to page2.html.
"""
import http.server
import os
import socket
import socketserver
import threading
import webbrowser

os.chdir(os.path.dirname(os.path.abspath(__file__)))
PORT = 8000


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Friendly routes: "/" -> index.html, "/page2" -> page2.html
        routes = {"/": "/index.html", "/index": "/index.html", "/page2": "/page2.html"}
        path = self.path.split("?")[0].split("#")[0]
        self.path = routes.get(path, self.path)
        return super().do_GET()


def local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except OSError:
        return "127.0.0.1"


socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as server:
    print("Birthday site is running! 🎂")
    print(f"  On this computer : http://localhost:{PORT}/")
    print(f"  On your phone    : http://{local_ip()}:{PORT}/  (same Wi-Fi)")
    print("Press Ctrl+C to stop.")
    threading.Timer(1, lambda: webbrowser.open(f"http://localhost:{PORT}/")).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
