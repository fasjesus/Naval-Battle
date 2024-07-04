import socket
import threading
import random

SIZE = 15
NUM_NAVIOS = 10
MAX_TENT = 20

def inicializa_campo():
    return [[' ' for _ in range(SIZE)] for _ in range(SIZE)]

def coloca_navios(campo):
    for _ in range(NUM_NAVIOS):
        while True:
            x = random.randint(0, SIZE - 1)
            y = random.randint(0, SIZE - 1)
            if campo[x][y] == ' ':
                campo[x][y] = 'S'
                break

def exibe_campo(campo):
    display = "\n" + "  " + " ".join([chr(c + ord('A')) for c in range(SIZE)]) + "\n"
    for i in range(SIZE):
        display += f"{i + 1:2} " + " ".join(campo[i]) + "\n"
    return display

def handle_client(conn, addr):
    print(f"Conexão estabelecida com {addr}")
    conn.sendall("\nBem-vindo ao jogo Batalha Naval!\n".encode('utf-8'))

    campo_cliente = inicializa_campo()
    campo_exibicao_cliente = inicializa_campo()
    coloca_navios(campo_cliente)

    campo_maquina = inicializa_campo()
    campo_exibicao_maquina = inicializa_campo()
    coloca_navios(campo_maquina)

    tentativas_cliente = 0
    tentativas_maquina = 0
    acertos_cliente = 0
    acertos_maquina = 0

    while tentativas_cliente < MAX_TENT and acertos_cliente < NUM_NAVIOS and acertos_maquina < NUM_NAVIOS:
        # Jogada do cliente
        data = conn.recv(1024).decode('utf-8')
        if not data or data.lower() == 'sair':
            break
        letra, numero = data.split()
        x = int(numero) - 1
        y = ord(letra.upper()) - ord('A')
        if 0 <= x < SIZE and 0 <= y < SIZE:
            if campo_maquina[x][y] == 'S':
                campo_exibicao_maquina[x][y] = 'O'
                conn.sendall("Acertou!\n".encode('utf-8'))
                acertos_cliente += 1
            else:
                campo_exibicao_maquina[x][y] = 'X'
                conn.sendall("Errou!\n".encode('utf-8'))
                tentativas_cliente += 1
        else:
            conn.sendall("Comando Inválido, Tente novamente\n".encode('utf-8'))
        conn.sendall(exibe_campo(campo_exibicao_maquina).encode('utf-8'))
        conn.sendall(f"Você já tentou: {tentativas_cliente} vezes\n".encode('utf-8'))

        # Jogada da máquina
        while True:
            x = random.randint(0, SIZE - 1)
            y = random.randint(0, SIZE - 1)
            if campo_cliente[x][y] == ' ' or campo_cliente[x][y] == 'S':
                break
        if campo_cliente[x][y] == 'S':
            campo_exibicao_cliente[x][y] = 'O'
            acertos_maquina += 1
        else:
            campo_exibicao_cliente[x][y] = 'X'
        tentativas_maquina += 1

    conn.sendall("\nFim de jogo!\n".encode('utf-8'))
    conn.sendall(f"Navios derrubados pelo cliente: {acertos_cliente}\n".encode('utf-8'))
    conn.sendall(f"Navios derrubados pela máquina: {acertos_maquina}\n".encode('utf-8'))
    conn.sendall("Campo do cliente:\n".encode('utf-8'))
    conn.sendall(exibe_campo(campo_exibicao_cliente).encode('utf-8'))
    conn.sendall("Campo da máquina:\n".encode('utf-8'))
    conn.sendall(exibe_campo(campo_exibicao_maquina).encode('utf-8'))
    conn.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 8080))
    server.listen(5)
    print("Servidor iniciado na porta 8080")
    while True:
        conn, addr = server.accept()
        threading.Thread(target=handle_client, args=(conn, addr)).start()

if __name__ == "__main__":
    main()
