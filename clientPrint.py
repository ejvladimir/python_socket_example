#!/usr/bin/python3

# Cliente que requisita constantemente a nota ao servidor



import socket
import time



# Executa para sempre
while(1):

    sock = socket.socket();

    # Socket em modo cliente não usa bind() nem listen(), só conecta.
    # 127.0.0.1 significa "esse computador". É chamado de endereço de loopback IPv4
    #   (porque também existe um equivalente em IPv6).
    sock.connect(('127.0.0.1', 8345));

    sock.sendall(bytes('R','utf8'));

    # Lê até 1024 bytes. Pode ser qualquer valor.
    nota = str(sock.recv(1024));

    print('Nota mais recente: ' + nota[2:-1]);

    sock.close()

    time.sleep(2);
