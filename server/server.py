import socket
import sys
import select
import os

BUF_SIZE = 1024
clients = dict()

#start tcp server and udp server
tcpS = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
udpS = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 19980)
udpS.bind(server_address)
tcpS.bind(server_address)
tcpS.listen(5)

#config select
inputs = [tcpS, udpS, sys.stdin]
runing = True

while True:
    readable, writable, exceptional = select.select(inputs, [], [])
    for socket in readable:
        if socket == tcpS:
            conn, tcpaddr = tcpS.accept()
            inputs.append(conn)
            print("new user added")
        elif socket == sys.stdin:
            runing = False
            break
        elif socket == udpS:
            data, udpaddr = socket.recvfrom(BUF_SIZE)
            data = str((int(data) + 1)).encode(encoding='UTF-8')
            socket.sendto(data, udpaddr)
        else:
            data = socket.recv(BUF_SIZE).decode("UTF-8")
            if data:
                if(socket in clients):
                    socket.sendall(data.encode(encoding='UTF-8'))
                else:
                    if data[0] == '0':
                        name = ''
                        index = 0
                        while(data[index + 1] != ' '):
                            name = name + data[index + 1]
                            index += 1
                        clients[socket] = name
                        print("client " + name + " added")
                        socket.sendall('1'.encode(encoding='UTF-8'))
                    else:
                        socket.sendall('0'.encode(encoding='UTF-8'))
            else:
                inputs.remove(socket)
                clients.pop(socket)
                socket.close()