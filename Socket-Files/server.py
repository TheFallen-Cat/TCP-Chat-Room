import os
from socket import socket
import threading

from numpy import true_divide


#trying to import the modules
try:
    import socket
except:
    os.system("pip install sockets")
    import sockets

HOST = 'localhost'
PORT = 9999

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((HOST, PORT))

server_socket.listen()


print("Server is up and running!")
#socket info
clients = []
nicknames = []

def broadcast(msg):

    for client in clients:
        client.send(msg)

def handle(client):

    while True:
        try:
            message = client.recv(1024)
            broadcast(message)

        except:
            index_of_client = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index_of_client]
            broadcast(f"{nickname} left the chat!\n".encode('ascii'))
            nicknames.remove(nickname)
            break



def RunServer():
    while True:
        connected_client, address = server_socket.accept()

        connected_client.send('NICK'.encode('ascii'))
        nickname = connected_client.recv(1024).decode('ascii')
        broadcast(f"{nickname} joined the chat!\n".encode('ascii'))

        nicknames.append(nickname)
        clients.append(connected_client)


        thread = threading.Thread(target=handle, args=(connected_client,))
        thread.start()


RunServer()