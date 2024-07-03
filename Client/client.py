import socket

def main():

    HOST = '172.26.6.67'
    PORT = 8080

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))  # Conecte na porta correta

    print("Digite 'sair' para encerrar a conexão.")

    while True:
        data = client.recv(1024).decode('utf-8')
        print(data)

        if "Fim de jogo" in data:
            break

        letra = input("Digite a letra: ")
        if letra.lower() == 'sair':
            print("Encerrando a conexão...")
            client.sendall(letra.encode('utf-8'))
            break

        numero = input("Digite o número: ")
        if numero.lower() == 'sair':
            print("Encerrando a conexão...")
            client.sendall(numero.encode('utf-8'))
            break

        client.sendall(f"{letra} {numero}".encode('utf-8'))

    client.close()

if __name__ == "__main__":
    main()
