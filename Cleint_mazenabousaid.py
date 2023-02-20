# By Mazen Abou Said with Prof Tajjedine
from socket import *
import datetime
import uuid
host ='127.0.0.1' #str(gethostbyname(gethostname())) works on private networks as Firewall Prevents Port Access by default on public networks
# we can use the localhost IP since both server and client run on same machine
port = 8696  # port number of the proxy server
client_socket = socket(AF_INET, SOCK_STREAM)  # instantiate socket to connect to proxy server
try:
    client_socket.connect((host, port))  # connect to the proxy server
    ipaddress = input("Input IP address of destination server: ")  # input ip to send to server
    client_socket.send(ipaddress.encode()) #sends to proxy
    request_timestamp = datetime.datetime.now()
    print("Request sent to server to connect to " + str(ipaddress) + " at " + str(request_timestamp))
    client_socket.settimeout(20) #waits for specific amount of time to receive response before breaking the connection with the Proxy Server and printing Request Time Out Using Except Below
    response = client_socket.recv(4096).decode() # receives 4096 bytes of data from server(limits data received to 2048 bytes)
    response_timestamp = datetime.datetime.now()
    print("At " + str(response_timestamp)+ " received:\n" + str(response))
    TimeTaken_timestamp = response_timestamp-request_timestamp #delta of first timestamp recorded and last timestamp recorded
    print("Total Time Taken: "+str(TimeTaken_timestamp.total_seconds()*1000) + " ms") # total round trip time after the client enters the IP address
    print("Mac Address: "+str(hex(uuid.getnode())))
except:
    print("Error: Request Time Out") # if any error print this
