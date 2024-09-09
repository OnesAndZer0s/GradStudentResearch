import socket
import mmWave as mm

SERVER_IP= "127.0.0.1"
SERVER_PORT = 5000



def main():
    # Create a socket object
    s = socket.socket()
    # connect to the server
    s.connect((SERVER_IP, SERVER_PORT))

    # Send the data to the server
    s.send(b"Hello server!")

    # Receive the data from the server
    print(s.recv(1024))

    # Close the connection
    s.close()
