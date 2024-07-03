import socket
import threading
import random

SIZE = 15
MAX_TENT = 20

def inicializa_campo():
    return [[' ' for _ in range(SIZE)] for _ in range(SIZE)]

def coloca_navios(campo):
    num_navios = 10
    for _ in range(num_navios):
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

def handle_client(conn, addr, campo, campo_exibicao):
    print(f"Conexão estabelecida com {addr}")
    conn.sendall("\n\nBem-vindo ao jogo Batalha Naval!\n".encode('utf-8'))  # Mensagem de boas-vindas
    tent = 0
    while tent < MAX_TENT:
        data = conn.recv(1024).decode('utf-8')
        if not data or data.lower() == 'sair':
            break
        try:
            letra, numero = data.split()
        except ValueError:
            conn.sendall("Entrada inválida. Por favor, forneça uma letra e um número.\n".encode('utf-8'))
            continue
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
    conn.sendall("\nFim de jogo! Aqui está o campo completo:\n".encode('utf-8'))
    conn.sendall(exibe_campo(campo).encode('utf-8'))
    conn.close()

def main():
    HOST = '0.0.0.0'
    PORT = 8080

    campo = inicializa_campo()
    campo_exibicao = inicializa_campo()
    coloca_navios(campo)
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    
    print("Servidor iniciado na porta 8080")
    while True:
        conn, addr = server.accept()
        threading.Thread(target=handle_client, args=(conn, addr, campo, campo_exibicao)).start()

if __name__ == "__main__":
    main()
