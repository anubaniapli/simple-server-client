import socket

#make a socket object
s = socket.socket()

#reserve a port for listening.
port = 12123

#bind the port but leave ip unrestricted
s.bind(('', port))
print("Socket bound to", port)

#put socket in listening mode. maximum of 5 possible waiting connections
s.listen(5)
print("Socket is listening")

#loop until user interrupt or error
while True:
    #establish connection with client
    c, addr = s.accept()
    print("Connection established with", addr)
    #encode in bytes and send a message.
    c.send("Connection Established. Welcome!".encode())
    c.close()
    #break after closing connection
    break


