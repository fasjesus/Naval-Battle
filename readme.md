# Batalha Naval - Jogo Cliente-Servidor

## Descrição

Este projeto implementa o jogo de Batalha Naval utilizando o modelo cliente-servidor em Python. O jogo é para um usuário vs computador, onde cada jogador tenta afundar os navios do adversário.

## Estrutura do Projeto

- Temos uma pasta para cada modalidade de conexão (Ethernet; LocalHost e Wifi) e cada uma delas contém os arquivos `client.py` e `server.py` com o IP adaptado conforme a sua modalidade.
- `game.py`: Módulo que contém a lógica principal do jogo (inicialização do campo, posicionamento dos navios, exibição do campo).
- `server.py`: Script do servidor que gerencia o estado do jogo e responde aos comandos do cliente.
- `client.py`: Script do cliente que se conecta ao servidor e permite ao usuário inserir suas tentativas.
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

Em outro terminal:

1. Navegue até a pasta `Client`:
   - cd Naval Battle/Client

2. Execute o script:
    - python client.py

### PARA VERIRIFICAR IP:

- ipconfig

exemplo:

Adaptador Ethernet Ethernet:

   Sufixo DNS específico de conexão. . . . . . : uesc.net
   Endereço IPv6 de link local . . . . . . . . : fe80::49e5:1c32:b9f0:b23d%18
   Endereço IPv4. . . . . . . .  . . . . . . . : 192.168.72.3
   Máscara de Sub-rede . . . . . . . . . . . . : 255.255.254.0
   Gateway Padrão. . . . . . . . . . . . . . . : 192.168.73.1

Adaptador de Rede sem Fio Wi-Fi:

   Sufixo DNS específico de conexão. . . . . . :
   Endereço IPv6 de link local . . . . . . . . : fe80::1b27:871a:2336:38eb%8
   Endereço IPv4. . . . . . . .  . . . . . . . : 172.26.11.205
   Máscara de Sub-rede . . . . . . . . . . . . : 255.255.192.0
   Gateway Padrão. . . . . . . . . . . . . . . : 172.26.0.1

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
	Evento: Cliente se conecta ao servidor.
	Estado: Esperando Conexão -> Esperando Entrada.
	Mensagem do Servidor para Cliente: "Bem-vindo ao jogo de Batalha Naval!"

2.	Recebendo Coordenadas do Cliente
	Evento: Cliente envia as coordenadas do tiro.
	Estado: Esperando Entrada -> Processando Tiro.
	Mensagem do Cliente para Servidor: "letra número" (ex: "A 1").

3.	Processando Tiro
	Evento: Servidor processa o tiro do cliente.
	Estado: Processando Tiro -> Esperando Entrada.
	Mensagens do Servidor para Cliente:
	"Acertou!" (se o tiro acertou um navio).
	"Errou!" (se o tiro errou).
	"Comando Inválido, Tente novamente" (se as coordenadas são inválidas).
	"Você já tentou: X vezes" (onde X é o número de tentativas).

4.	Exibição do Campo
	Evento: Servidor envia o estado atual do campo para o cliente após cada tiro.
	Estado: Processando Tiro -> Esperando Entrada.
	Mensagem do Servidor para Cliente: Estado atual do campo de jogo.

5.	Jogo Encerrado
	Evento: Cliente atinge o número máximo de tentativas ou acerta todos os navios.
	Estado: Qualquer estado -> Jogo Encerrado.
	Mensagens do Servidor para Cliente:
	"Fim de jogo! Aqui está o campo completo:"
	Estado final do campo de jogo.

Estrutura do Protocolo
Estrutura de Mensagens
1.	Mensagem de Boas-vindas:
	Formato: "Bem-vindo ao jogo de Batalha Naval!"

2.	Mensagem de Coordenadas:
	Formato: "letra número" (ex: "A 1")

3.	Mensagem de Resultado do Tiro:
	Formato: "Acertou!", "Errou!", ou "Comando Inválido, Tente novamente"

4.	Mensagem de Estado do Campo:
	Formato: Representação textual do campo de jogo.

5.	Mensagem de Tentativas:
	Formato: "Você já tentou: X vezes"

6.	Mensagem de Fim de Jogo:
	Formato: "Fim de jogo! Aqui está o campo completo:" + Estado final do campo de jogo.

### Funcionamento do Jogo

- Cada jogador tem 20 tentativas para acertar os navios do adversário.
- O tabuleiro é de 15x15 e contém 10 navios posicionados aleatoriamente.
- O servidor gerencia o estado do jogo e o tabuleiro para cada cliente conectado.

### Colaboradores
- Brenda `Brendacas`
- Flávia `fasjesus`
- Isaac `inlima`
- Laiz `laizcruz`
