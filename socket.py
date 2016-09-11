import socket

mysock = socket.socket(socket.AF_INET, sock.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))