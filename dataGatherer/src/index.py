import socket
import time
import mmWave as mm
import asyncio


from serialNumber import *

UID = getserial()
SERVER_IP= "127.0.0.1"
SERVER_PORT = 5001


async def main():
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('', 4242))

    # s.bind((SERVER_IP, SERVER_PORT))
    s.connect((SERVER_IP, SERVER_PORT))
    for i in range(10):
        s.send("Hello".encode())

asyncio.run(main())