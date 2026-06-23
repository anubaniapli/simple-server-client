import socket

#make a socket object
s = socket.socket()

#select the port to connect to
port = 12123

#connect to server on local computer
s.connect(('ip_addr', port))

#recieve up to 1024 bytes data from server
print(s.recv(1024))

#close connection
s.close()


