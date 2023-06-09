import socket

# server socket will work with IPv4 and use TCP
# socket will be bind with special addres 127.0.0.1 (localhost) and port 8.8.8.8

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 8888))

server_socket.listen() 

# in this cycle, we will constantly monitor for connectivity

while True:
    try:
        application_socket, application_address = server_socket.accept()

    except:
        server_socket.close()
    
    else:

        # when the socket gets connected it starts accepting incoming data

        recv_data = application_socket.recv(1024).decode('utf-8').split(':')
        application_socket.close()

        print(recv_data)