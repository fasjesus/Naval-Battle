import socket

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 8080))

    while True:
        data = client.recv(1024).decode('utf-8')
        print(data)
        if "Fim de jogo" in data:
            break
        if "Sua vez!" in data:
            letra = input("Digite a letra: ")
            numero = input("Digite o número: ")
            client.sendall(f"{letra} {numero}".encode('utf-8'))
    client.close()

if __name__ == "__main__":
    main()
