import random
import os

SIZE = 15
MAX_TENT = 20

def inicializa_campo():
    return [[' ' for _ in range(SIZE)] for _ in range(SIZE)]

def coloca_navios(campo):
    num_navios = 10  # Defina quantos navios você deseja
    for _ in range(num_navios):
        x = random.randint(0, SIZE - 1)
        y = random.randint(0, SIZE - 1)
        campo[x][y] = 'S'

def exibe_campo(campo):
    print("  ", end="")
    for c in range(SIZE):
        print(chr(c + ord('A')), end=" ")
    print()
    
    for i in range(SIZE):
        print(f"{i + 1:2}", end=" ")
        for j in range(SIZE):
            print(campo[i][j], end=" ")
        print()

def main():
    campo = inicializa_campo()
    campo_exibicao = inicializa_campo()
    tent = 0

    coloca_navios(campo)

    os.system('cls' if os.name == 'nt' else 'clear')
    print("Você tem 20 jogadas")
    print("Tente encontrar os navios")
    print("O = ACERTOU \nX = ERROU \n")

    while tent < MAX_TENT:
        os.system('cls' if os.name == 'nt' else 'clear')
        exibe_campo(campo_exibicao)
        print(f"\nVocê já tentou: {tent} vezes\n")

        letra = input("Digite a letra: ").upper()
        numero = int(input("Digite o número: "))

        x = numero - 1
        y = ord(letra) - ord('A')

        if 0 <= x < SIZE and 0 <= y < SIZE:
            if campo[x][y] == 'S':
                campo_exibicao[x][y] = 'O'
                print("Acertou!")
            else:
                campo_exibicao[x][y] = 'X'
                print("Errou!")
            tent += 1
        else:
            print("Comando Inválido, Tente novamente")

        input("\nPressione qualquer tecla para continuar...")

    os.system('cls' if os.name == 'nt' else 'clear')
    print("Fim de jogo! Aqui está o campo completo:")
    exibe_campo(campo)

if __name__ == "__main__":
    main()