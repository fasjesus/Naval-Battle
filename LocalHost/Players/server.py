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
    display = "  " + " ".join([chr(c + ord('A')) for c in range(SIZE)]) + "\n"
    for i in range(SIZE):
        display += f"{i + 1:2} " + " ".join(campo[i]) + "\n"
    return display

def handle_client(conn, addr, player_num, campos, campos_exibicao, turns, players):
    conn.sendall(f"Você é o Jogador {player_num + 1}\n".encode('utf-8'))
    tent = 0
    while tent < MAX_TENT:
        if turns[0] != player_num:
            conn.sendall("Aguarde sua vez...\n".encode('utf-8'))
            continue
        conn.sendall("Sua vez! Digite a letra e o número do tiro (ex: A1): ".encode('utf-8'))
        data = conn.recv(1024).decode('utf-8')
        if not data:
            break
        letra, numero = data.split()
        x = int(numero) - 1
        y = ord(letra.upper()) - ord('A')
        if 0 <= x < SIZE and 0 <= y < SIZE:
            if campos[1 - player_num][x][y] == 'S':
                campos_exibicao[1 - player_num][x][y] = 'O'
                conn.sendall("Acertou!\n".encode('utf-8'))
            else:
                campos_exibicao[1 - player_num][x][y] = 'X'
                conn.sendall("Errou!\n".encode('utf-8'))
                tent += 1
        else:
            conn.sendall("Comando Inválido, Tente novamente\n".encode('utf-8'))
            continue
        turns[0] = 1 - player_num
        conn.sendall(exibe_campo(campos_exibicao[1 - player_num]).encode('utf-8'))
        conn.sendall(f"Você já tentou: {tent} vezes\n".encode('utf-8'))
    conn.sendall("Fim de jogo! Aqui está o campo completo:\n".encode('utf-8'))
    conn.sendall(exibe_campo(campos[1 - player_num]).encode('utf-8'))
    players[0].close()
    players[1].close()

def main():
    campos = [inicializa_campo(), inicializa_campo()]
    campos_exibicao = [inicializa_campo(), inicializa_campo()]
    coloca_navios(campos[0])
    coloca_navios(campos[1])
    
    turns = [0]  # Lista para manter a sincronia dos turnos
    players = [None, None]

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 8080))
    server.listen(2)
    print("Servidor iniciado na porta 8080, aguardando dois jogadores...")

    for i in range(2):
        conn, addr = server.accept()
        players[i] = conn
        threading.Thread(target=handle_client, args=(conn, addr, i, campos, campos_exibicao, turns, players)).start()

if __name__ == "__main__":
    main()
