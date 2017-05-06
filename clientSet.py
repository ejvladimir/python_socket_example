#!/usr/bin/python3

# Cliente que requisita constantemente a nota ao servidor



import socket
import time



# Executa para sempre
while(1):

    nota = input('Insira nova nota: ');

    sock = socket.socket();

    # Socket em modo cliente não usa bind() nem listen(), só conecta.
    # 127.0.0.1 significa "esse computador". É chamado de endereço de loopback IPv4
    #   (porque também existe um equivalente em IPv6).
    sock.connect(('127.0.0.1', 8345));

    sock.sendall(bytes('W'+str(nota),'utf8'));

    sock.close()
