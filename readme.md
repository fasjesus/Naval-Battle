# Batalha Naval - Jogo Cliente-Servidor

## Descrição

Este projeto implementa o jogo de Batalha Naval utilizando o modelo cliente-servidor em Python. O jogo é para um usuário vs computador, onde cada jogador tenta afundar os navios do adversário.

## Estrutura do Projeto

- `Game/game.py`: Módulo que contém a lógica principal do jogo (inicialização do campo, posicionamento dos navios, exibição do campo).
- `Server/server.py`: Script do servidor que gerencia o estado do jogo e responde aos comandos do cliente.
- `Client/client.py`: Script do cliente que se conecta ao servidor e permite ao usuário inserir suas tentativas.
- `README.md`: Documentação do projeto.

## Como Executar

### Requisitos
- Python 3.x

### Passos para Executar o Servidor

1. Navegue até a pasta `Server`:
   - cd Naval Battle/Server

2. Execute o script:
    - python server.py

### Passos para Executar o Cliente

1. Navegue até a pasta `Client`:
   - cd Naval Battle/Client

2. Execute o script:
    - python client.py

### Protocolo de Comunicação

- O servidor e o cliente se comunicam através de sockets TCP.
- O cliente envia comandos no formato: <letra> <número>.
- O servidor responde com mensagens indicando se o jogador acertou ou errou e atualiza o estado do tabuleiro.

### Protocolo de Aplicação 
Estados do Jogo
1.	Esperando Conexão: O servidor está esperando conexões de clientes.
2.	Esperando Entrada: O servidor está esperando a entrada do cliente (coordenadas do tiro).
3.	Processando Tiro: O servidor está processando o tiro do cliente.
4.	Jogo Encerrado: O jogo terminou (cliente atingiu todos os navios ou esgotou as tentativas).

Eventos e Mensagens
1.	Conexão do Cliente
o	Evento: Cliente se conecta ao servidor.
o	Estado: Esperando Conexão -> Esperando Entrada.
o	Mensagem do Servidor para Cliente: "Bem-vindo ao jogo de Batalha Naval!"

2.	Recebendo Coordenadas do Cliente
o	Evento: Cliente envia as coordenadas do tiro.
o	Estado: Esperando Entrada -> Processando Tiro.
o	Mensagem do Cliente para Servidor: "letra número" (ex: "A 1").

3.	Processando Tiro
o	Evento: Servidor processa o tiro do cliente.
o	Estado: Processando Tiro -> Esperando Entrada.
o	Mensagens do Servidor para Cliente:
o	"Acertou!" (se o tiro acertou um navio).
o	"Errou!" (se o tiro errou).
o	"Comando Inválido, Tente novamente" (se as coordenadas são inválidas).
o	"Você já tentou: X vezes" (onde X é o número de tentativas).

4.	Exibição do Campo
o	Evento: Servidor envia o estado atual do campo para o cliente após cada tiro.
o	Estado: Processando Tiro -> Esperando Entrada.
o	Mensagem do Servidor para Cliente: Estado atual do campo de jogo.

5.	Jogo Encerrado
o	Evento: Cliente atinge o número máximo de tentativas ou acerta todos os navios.
o	Estado: Qualquer estado -> Jogo Encerrado.
o	Mensagens do Servidor para Cliente:
o	"Fim de jogo! Aqui está o campo completo:"
o	Estado final do campo de jogo.

Estrutura do Protocolo
Estrutura de Mensagens
1.	Mensagem de Boas-vindas:
o	Formato: "Bem-vindo ao jogo de Batalha Naval!"

2.	Mensagem de Coordenadas:
o	Formato: "letra número" (ex: "A 1")

3.	Mensagem de Resultado do Tiro:
o	Formato: "Acertou!", "Errou!", ou "Comando Inválido, Tente novamente"

4.	Mensagem de Estado do Campo:
o	Formato: Representação textual do campo de jogo.

5.	Mensagem de Tentativas:
o	Formato: "Você já tentou: X vezes"

6.	Mensagem de Fim de Jogo:
o	Formato: "Fim de jogo! Aqui está o campo completo:" + Estado final do campo de jogo.

### Funcionamento do Jogo

- Cada jogador tem 20 tentativas para acertar os navios do adversário.
- O tabuleiro é de 15x15 e contém 10 navios posicionados aleatoriamente.
- O servidor gerencia o estado do jogo e o tabuleiro para cada cliente conectado.

### Colaboradores
- Brenda `Brendacas`
- Flávia `fasjesus`
- Isaac `inlima`
- Laiz `laizcruz`
