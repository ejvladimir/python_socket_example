#!/usr/bin/python3

# Servidor que vai armazenar as informações e trocar com os clientes

class aluno:
    def __init__(self, nome, nota):
        self.nome = nome;
        self.nota = nota;

    def setNota(self, nota):
        self.nota = nota;


import socket

jean = aluno("Jean", 12);

# Cria o socket.
# O padrão é criar um socket TCP. Tu também poderia criar um socket UDP.
# TCP - correção de erros no envio, mas o pacote é maior. Tu usa se quiser que a informação chegue.
# UDP - foda-se se não deu certo, continua enviando. O pacote é menor e é muito melhor pra stream de dados,
#   tipo um jogo rápido como CS, LOL, etc. Pra stream de vídeo ao vivo e de rádio on-line por exemplo é bem melhor.
sock = socket.socket();

sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Abre o socket em todas as interfaces na porta 8345
# Se tu tiver duas interfaces de rede (por exemplo, Wi-Fi e ethernet) conectadas
#   ao mesmo tempo, tu vai ter dois endereços de rede, um pra cada interface.
#   O primeiro elemento dessa tuple é o endereço no qual o socket deve "ouvir".
#   Assim, tu poderia deixar o servidor acessível somente pela Wi-Fi por exemplo.
#   0.0.0.0 significa "todos os endereços", portanto, todas as interfaces.
# Se o endereço fosse a rua de uma casa, a porta seria o número dessa casa.
#   Eu escolhi esse número aleatoriamente, mas alguns serviços tem portas específicas.
#   Servidores http usam a porta 80 como padrão, ftp é 21, ssh é 22, etc...
sock.bind(('0.0.0.0', 8345));

# Começa a ouvir por conexões no socket. Vai deixar até 2 conexões na fila antes
#   de serem aceitas. O resto vai ser rejeitado.
sock.listen(2);

# Executa para sempre
while(1):

    # Espera uma conexão. Uma conexão vai criar um novo socket (conexao) em que
    #   se pode ler e escrever dados.
    # Recebe uma tuple com o socket e o endereço de quem se conectou. Da pra
    #   ignorar o endereço e usar só o socket.
    conexao, cliente = sock.accept()

    # Lê até 1024 bytes. Pode ser qualquer valor.
    dados = str(conexao.recv(1024))[2:-1];
    print("Comando recebido: " + dados);

    # O programa vai aceitar 2 comandos: "W" para escrever a nota e "R" para ler
    if(dados[0] == 'W'):
        jean.setNota( float(dados[1:]) );

    if(dados[0] == 'R'):
        conexao.sendall(bytes(str(jean.nota), 'utf8') );

    conexao.close()
