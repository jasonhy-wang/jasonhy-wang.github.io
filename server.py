import http.server
import socketserver
import hupper

def start_server():
    PORT = 8000
    Handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()

if __name__ == "__main__":
    if hupper.is_active():
        # If hupper is active, just start the server
        start_server()
    else:
        # If hupper is not active, start it and then start the server
        hupper.start_reloader('server.start_server')
