import socketserver
import threading

SERVER_IP= "127.0.0.1"
SERVER_PORT = 5000

class ServerHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        fin = open("../website/index.html")
        self.request.sendall(('HTTP/1.0 200 OK\n\n' + fin.read()).encode())
        fin.close()

class DataStreamHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print(self.client_address)
        self.data = self.request[0].strip()
        
        print(self.data)



def main():
    try:
        webServer = socketserver.TCPServer((SERVER_IP, SERVER_PORT), ServerHandler)
        dataSocket = socketserver.UDPServer((SERVER_IP, 5001), DataStreamHandler)
        server_thread = threading.Thread(target=webServer.serve_forever)
        other_thread = threading.Thread(target=dataSocket.serve_forever)
        server_thread.daemon = True
        other_thread.daemon = True
        server_thread.start()
        other_thread.start()
        print("Server loop running in thread:", server_thread.name)
        server_thread.join()
        other_thread.join()
    except KeyboardInterrupt: # this is needed to stop the server
        print("Shutting down server")
        webServer.shutdown()
        webServer.server_close()
        dataSocket.shutdown()
        dataSocket.server_close()

if __name__ == "__main__":
    main()


