import socket

 

msgFromClient       = "0DAMIT 0"

bytesToSend         = str.encode(msgFromClient)

serverAddressPort   = ("localhost", 19980)

bufferSize          = 1024

 

# Create a UDP socket at client side

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

 

# Send to server using created UDP socket

UDPClientSocket.sendto(bytesToSend, serverAddressPort)

 

msgFromServer = UDPClientSocket.recvfrom(bufferSize)

 

msg = "Message from Server "+msgFromServer[0].decode("UTF-8")

print(msg)