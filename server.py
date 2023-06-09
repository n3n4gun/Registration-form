import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 8888))

server_socket.listen()

while True:
    try:
        application_socket, application_address = server_socket.accept()

    except:
        server_socket.close()
    
    else:
        recv_data = application_socket.recv(1024).decode('utf-8').split(':')
        application_socket.close()

        print(recv_data)