import socket
import psycopg2
import uuid

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

        print(f'Connection with {application_address} is installed')

        # when the socket gets connected it starts accepting incoming data
        try:
            db_connection = psycopg2.connect(dbname = 'registration_db', host = '127.0.0.1', user = 'postgres', password = '12345', port = '5432')

            print('Connection with database is installed!')

            db_curs = db_connection.cursor()

            recv_data = application_socket.recv(1024).decode('utf-8').split(':')

            try:

                db_curs.execute("INSERT INTO users (user_id, user_name, user_surname, user_email, user_password) VALUES (%s, %s, %s, %s, %s)", (str(uuid.uuid4()), recv_data[0], recv_data[1], recv_data[2], recv_data[3]))
                db_connection.commit()

                print('Data was appended in database!')

                application_socket.send('Data was appended in database!'.encode('utf-8'))

            except:
                print('Server error!')

            else:

                db_curs.close()
                db_connection.close()

                application_socket.close()

        except:
            print('Connection is failed!')