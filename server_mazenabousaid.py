# By Mazen Abou Said with Prof Tajjedine
import datetime
from socket import *
host = '127.0.0.1' #str(gethostbyname(gethostname())) works on private networks as Firewall Prevents Port Access by default on public networks
# we can use the localhost IP since both server and client run on same machine
port = 8696 # port the server binds to
server_socket = socket(AF_INET, SOCK_STREAM) # instantiate tcp socket
server_socket.bind((host, port))  # bind host address and port together
server_socket.listen() # listens for incoming connections

try:
    connection, address = server_socket.accept() # produces a tuple: in server_socket.accept()[0] we have connection type info, in [1] we have the IP and Port info
    print("TCP Connection established from " + str(address)+" at " + str(datetime.datetime.now()))
    ip_request = connection.recv(1024).decode() # Decode IP Address Request Message from Client
    print("Request from client to connect to " + str(ip_request) + " at " + str(datetime.datetime.now()))
    dest_socket= socket(AF_INET, SOCK_STREAM) # creates new socket to connect to destination server
    dest_socket.connect((str(ip_request),80)) # connects to requested destination server via port 80(web)
    print("Connection to Destination Server established at " + str(datetime.datetime.now()))
    dest_socket.send(bytes("GET / HTTP/1.1\r\nHost:"+str(ip_request)+":80\r\n\r\n",'utf-8')) # requests page data using GET Method
    dest_socket.settimeout(20) # waits for specific amount of time to receive response before breaking the connection with the destination server and printing Request Time Out Using Except Below
    req=dest_socket.recv(4096) # receives back response
    print("Response received from destination server at "+str(datetime.datetime.now()))
    connection.send(req) # sends response to client
    print("Response sent to destination server at " + str(datetime.datetime.now()))

except:
    print("Error: Request Time Out")# if any error print this
