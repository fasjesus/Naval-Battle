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
    header = "  " + " ".join([chr(c + ord('A')) for c in range(SIZE)]) + "\n"
    display = header
    for i in range(SIZE):
        row_number = f"{i + 1:2} "
        row_content = " ".join(campo[i])
        display += row_number + row_content + "\n"
    return display

def handle_client(conn, addr):
    print(f"Conexão estabelecida com {addr}")
    conn.sendall("\nBem-vindo ao jogo Batalha Naval!\n".encode('utf-8'))

    campo_cliente = inicializa_campo()
    campo_exibicao_cliente = inicializa_campo()
    coloca_navios(campo_cliente)

    tentativas_cliente = 0
    acertos_cliente = 0
    coordenadas_usadas_cliente = set()

    while tentativas_cliente < MAX_TENT and acertos_cliente < NUM_NAVIOS:
        # Jogada do cliente
        while True:
            data = conn.recv(1024).decode('utf-8')
            if not data or data.lower() == 'sair':
                conn.close()
                return
            try:
                letra, numero = data.split()
                x = int(numero) - 1
                y = ord(letra.upper()) - ord('A')
                if 0 <= x < SIZE and 0 <= y < SIZE:
                    if (x, y) not in coordenadas_usadas_cliente:
                        coordenadas_usadas_cliente.add((x, y))
                        break
                    else:
                        conn.sendall("Coordenadas já escolhidas, tente novamente\n".encode('utf-8'))
                else:
                    conn.sendall("Comando inválido, tente novamente\n".encode('utf-8'))
            except ValueError:
                conn.sendall("Formato inválido, use <letra> <número>\n".encode('utf-8'))

        mensagens = ""
        if campo_cliente[x][y] == 'S':
            campo_exibicao_cliente[x][y] = 'O'
            mensagens += "Acertou!\n"
            acertos_cliente += 1
        else:
            campo_exibicao_cliente[x][y] = 'X'
            mensagens += "Errou!\n"
            tentativas_cliente += 1
        
        mensagens += exibe_campo(campo_exibicao_cliente)
        mensagens += f"Você já tentou: {tentativas_cliente} vezes\n"
        conn.sendall(mensagens.encode('utf-8'))

    mensagens = "\nFim de jogo!\n"
    mensagens += f"Navios derrubados pelo cliente: {acertos_cliente}\n"
    mensagens += "Campo do cliente:\n"
    mensagens += exibe_campo(campo_exibicao_cliente)
    mensagens += "Campo completo:\n"
    mensagens += exibe_campo(campo_cliente)
    conn.sendall(mensagens.encode('utf-8'))
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
