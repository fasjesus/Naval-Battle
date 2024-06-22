# O servidor será responsável por configurar o jogo, gerenciar o estado do tabuleiro e responder aos comandos do cliente.
import socket
import threading
import random

SIZE = 15
MAX_TENT = 20

def inicializa_campo():
    return [[' ' for _ in range(SIZE)] for _ in range(SIZE)]

def coloca_navios(campo):
    num_navios = 10  # Defina quantos navios voc� deseja
    for _ in range(num_navios):
        x = random.randint(0, SIZE - 1)
        y = random.randint(0, SIZE - 1)
        campo[x][y] = 'S'

def exibe_campo(campo):
    display = "  " + " ".join([chr(c + ord('A')) for c in range(SIZE)]) + "\n"
    for i in range(SIZE):
        display += f"{i + 1:2} " + " ".join(campo[i]) + "\n"
    return display

def handle_client(conn, addr, campo, campo_exibicao):
    print(f"Conexão estabelecida com {addr}")
    tent = 0

    while tent < MAX_TENT:
        data = conn.recv(1024).decode('utf-8')
        if not data:
            break

        letra, numero = data.split()
        x = int(numero) - 1
        y = ord(letra.upper()) - ord('A')

        if 0 <= x < SIZE and 0 <= y < SIZE:
            if campo[x][y] == 'S':
                campo_exibicao[x][y] = 'O'
                conn.sendall("Acertou!\n".encode('utf-8'))
            else:
                campo_exibicao[x][y] = 'X'
                conn.sendall("Errou!\n".encode('utf-8'))
            tent += 1
        else:
            conn.sendall("Comando Inválido, Tente novamente\n".encode('utf-8'))

        conn.sendall(exibe_campo(campo_exibicao).encode('utf-8'))
        conn.sendall(f"Você já tentou: {tent} vezes\n".encode('utf-8'))

    conn.sendall("Fim de jogo! Aqui está o campo completo:\n".encode('utf-8'))
    conn.sendall(exibe_campo(campo).encode('utf-8'))
    conn.close()

def main():
    campo = inicializa_campo()
    campo_exibicao = inicializa_campo()
    coloca_navios(campo)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 5555))
    server.listen(5)
    print("Servidor iniciado na porta 5555")

    while True:
        conn, addr = server.accept()
        threading.Thread(target=handle_client, args=(conn, addr, campo, campo_exibicao)).start()

if __name__ == "__main__":
    main()