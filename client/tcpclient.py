import socket 

#创建套接字
tcpClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('socket---%s'%tcpClientSocket)
#链接服务器
serverAddr = ('localhost',19980)
tcpClientSocket.connect(serverAddr)
print('connect success!')

    #发送数据

tcpClientSocket.sendall('0你好 0'.encode())  

    #接收数据
recvData = tcpClientSocket.recv(1024)
    #打印接收到的数据
print('the receive message is:' + recvData.decode())

#关闭套接字
tcpClientSocket.close()
print('close socket!')