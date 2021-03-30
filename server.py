from http.server import HTTPServer, CGIHTTPRequestHandler, BaseHTTPRequestHandler
import os

class ClassStartServer():

    def start_serv():
        # path to file 'index.html'
        DIR = 'template'

        # move to directory
        os.chdir(DIR)

        # servert settings (ip, port)
        server_address = ("localhost", 8000)
        httpd = HTTPServer(server_address, CGIHTTPRequestHandler, 'template/index.html')
        print("Server startup was successful")
        print("You can go to the page at this address: 127.0.0.1:8000/")
        httpd.serve_forever()