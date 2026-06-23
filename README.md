# A Simple Server-Client Program

## Introduction

Behind the web browsing experience is a server and a client. The server listens and replies when the client reaches out. A socket is a low level networking interface. This will be a reconstruction of the most basic server and client programs in python. It will be barebones with nothing extra such as a web page, merely the connection between two sockets.

## Server

A server has several methods that allow it to perform its function. The `bind()` method restricts connections to certain IPs or ports. The `listen()` method allows the server to recognize incoming connections. The `accept()` and `close()` methods control whether or not the server allows a connection to be established and when that connection gets terminated. The steps are rather straightforward.

* Import the socket module.

* Make a socket object.

* Reserve a port to listen on.

* Bind that port but leave the ip address unrestricted by passing an empty string.  

* Place the server into listening mode.

* Construct a while loop that will accept all incoming connections and close those connections after a welcome message.

## Client

You can test if the server is working by using telnet. `telnet localhost port` where localhost is your ip address and port is where the server is listening. Now for the client side the steps are even simpler than the server.

* Import socket module and make a socket object.

* Connect to server on localhost. Replace `'ip_addr'` with your PC's IP address.

* Recieve data and close the connection.

## Usage

For ease of use open two terminals and run the server script and the client script in different terminals.

`python simple-server.py`

![](https://github.com/anubaniapli/simple-server-client/blob/main/simple-server.png))

`python simple-client.py`

![](https://github.com/anubaniapli/simple-server-client/blob/main/simple-client.png)
