# Batalha Naval - Jogo Cliente-Servidor

## Descrição

Este projeto implementa o jogo de Batalha Naval utilizando o modelo cliente-servidor em Python. O jogo é para dois jogadores, onde cada jogador tenta afundar os navios do adversário.

## Estrutura do Projeto

- `Game/game.py`: Módulo que contém a lógica principal do jogo (inicialização do campo, posicionamento dos navios, exibição do campo).
- `Server/server.py`: Script do servidor que gerencia o estado do jogo e responde aos comandos do cliente.
- `Client/client.py`: Script do cliente que se conecta ao servidor e permite ao usuário inserir suas tentativas.
- `README.md`: Documentação do projeto.

## Como Executar

### Requisitos
- Python 3.x

### Passos para Executar o Servidor

1. Navegue até a pasta `server`:
   cd Naval Battle/Server

2. Execute o script:
    python server.py

### Passos para Executar o Cliente

1. Navegue até a pasta `Client`:
   cd Naval Battle/Client

2. Execute o script:
    python client.py

### Protocolo de Comunicação

O servidor e o cliente se comunicam através de sockets TCP.
O cliente envia comandos no formato: <letra> <número>.
O servidor responde com mensagens indicando se o jogador acertou ou errou e atualiza o estado do tabuleiro.

### Funcionamento do Jogo

Cada jogador tem 20 tentativas para acertar os navios do adversário.
O tabuleiro é de 15x15 e contém 10 navios posicionados aleatoriamente.
O servidor gerencia o estado do jogo e o tabuleiro para cada cliente conectado.

### Contribuidores
Brenda
Flávia
Isaac
Laiz