import random
import os

SIZE = 15
MAX_TENT = 20
NUM_NAVIOS = 10

def inicializa_campo():
    return [[' ' for _ in range(SIZE)] for _ in range(SIZE)]

def coloca_navios(campo, num_navios=NUM_NAVIOS):
    for _ in range(num_navios):
        while True:
            x = random.randint(0, SIZE - 1)
            y = random.randint(0, SIZE - 1)
            if campo[x][y] == ' ':
                campo[x][y] = 'S'
                break

def exibe_campo(campo, revelar_navios=False):
    print("  ", end="")
    for c in range(SIZE):
        print(chr(c + ord('A')), end=" ")
    print()
    
    for i in range(SIZE):
        print(f"{i + 1:2}", end=" ")
        for j in range(SIZE):
            if not revelar_navios and campo[i][j] == 'S':
                print(' ', end=" ")
            else:
                print(campo[i][j], end=" ")
        print()

def jogada_maquina(campo):
    while True:
        x = random.randint(0, SIZE - 1)
        y = random.randint(0, SIZE - 1)
        if campo[x][y] not in ['O', 'X']:
            return x, y

def entrada_valida(letra, numero):
    if len(letra) != 1 or letra not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        return False
    if not numero.isdigit() or not (1 <= int(numero) <= SIZE):
        return False
    return True

def main():
    campo_jogador = inicializa_campo()
    campo_exibicao_jogador = inicializa_campo()
    campo_maquina = inicializa_campo()
    campo_exibicao_maquina = inicializa_campo()
    tent = 0

    coloca_navios(campo_jogador)
    coloca_navios(campo_maquina)

    os.system('cls' if os.name == 'nt' else 'clear')
    print("Você tem 20 jogadas para encontrar os navios da máquina")
    print("O = ACERTOU \nX = ERROU \n")

    while tent < MAX_TENT:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Seu campo:")
        exibe_campo(campo_exibicao_jogador, revelar_navios=False)
        print(f"\nVocê já tentou: {tent} vezes\n")

        letra = input("Digite a letra (A-Z): ").upper()
        numero = input("Digite o número (1-15): ")

        if entrada_valida(letra, numero):
            x = int(numero) - 1
            y = ord(letra) - ord('A')

            if 0 <= x < SIZE and 0 <= y < SIZE:
                if campo_maquina[x][y] == 'S':
                    campo_exibicao_jogador[x][y] = 'O'
                    print("Acertou!")
                else:
                    campo_exibicao_jogador[x][y] = 'X'
                    print("Errou!")
                tent += 1
            else:
                print("Comando Inválido, Tente novamente")
        else:
            print("Entrada inválida. Certifique-se de que a letra está entre A e Z e o número entre 1 e 15.")

        if tent < MAX_TENT:
            x_maquina, y_maquina = jogada_maquina(campo_maquina)
            if campo_jogador[x_maquina][y_maquina] == 'S':
                campo_exibicao_maquina[x_maquina][y_maquina] = 'O'
                print(f"\nA máquina acertou na coordenada {chr(y_maquina + ord('A'))}{x_maquina + 1}!")
            else:
                campo_exibicao_maquina[x_maquina][y_maquina] = 'X'
                print(f"\nA máquina errou na coordenada {chr(y_maquina + ord('A'))}{x_maquina + 1}!")

        input("\nPressione qualquer tecla para continuar...")

    os.system('cls' if os.name == 'nt' else 'clear')
    print("Fim de jogo! Aqui está o campo completo:")
    print("Seu campo:")
    exibe_campo(campo_jogador, revelar_navios=True)
    print("\nCampo da máquina:")
    exibe_campo(campo_maquina, revelar_navios=True)

if __name__ == "__main__":
    main()