# Documentação do Protocolo e Funcionamento do Software

## Propósito do Software

O software implementa um jogo de Batalha Naval onde o cliente tenta afundar os navios escondidos no campo do servidor. O servidor gerencia o jogo, incluindo a inicialização do campo de batalha, posicionamento dos navios e controle das jogadas do cliente. O cliente se conecta ao servidor, envia suas jogadas (coordenadas) e recebe o estado atualizado do campo, incluindo se acertou ou errou o tiro.

## Motivação da Escolha do Protocolo de Transporte

O protocolo de transporte utilizado é o TCP (Transmission Control Protocol). A escolha do TCP se dá pela necessidade de uma comunicação confiável e sequencial entre o cliente e o servidor. No contexto de um jogo, é crucial que todas as mensagens sejam entregues na ordem correta e sem perdas para manter a integridade do estado do jogo.

## Estrutura do Projeto

- Temos uma pasta para cada modalidade de conexão (Ethernet; LocalHost e Wifi) e cada uma delas contém os arquivos `client.py` e `server.py` com o IP adaptado conforme a sua modalidade.
- `game.py`: Módulo que contém a lógica principal do jogo (inicialização do campo, posicionamento dos navios, exibição do campo).
- `server.py`: Script do servidor que gerencia o estado do jogo e responde aos comandos do cliente.
- `client.py`: Script do cliente que se conecta ao servidor e permite ao usuário inserir suas tentativas.
- `README.md`: Documentação do projeto.

## Como Executar

### Requisitos Mínimos de Funcionamento
- Python 3.6 ou superior
- Módulo socket para comunicação em rede
- Módulo threading para gerenciar múltiplas conexões de clientes simultâneas no servidor

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

### Protocolo de Comunicação (resumo)

- O servidor e o cliente se comunicam através de sockets TCP.
- O cliente envia comandos no formato: <letra> <número>.
- O servidor responde com mensagens indicando se o jogador acertou ou errou e atualiza o estado do tabuleiro.

### Protocolo da Camada de Aplicação 

Eventos e Estados

1. Conexão Iniciada:
- Servidor: Aceita conexão de um cliente.
- Cliente: Estabelece conexão com o servidor.

2. Inicialização do Jogo:
- Servidor: Envia mensagem de boas-vindas ao cliente e inicializa o campo de batalha.
- Cliente: Recebe mensagem de boas-vindas.

3. Jogada do Cliente:
- Cliente: Envia coordenadas da jogada ao servidor.
- Servidor: Recebe coordenadas, verifica se é um acerto ou erro, atualiza o estado do jogo e envia a resposta ao cliente.

4. Atualização do Estado do Jogo:
- Servidor: Envia estado atualizado do campo de batalha ao cliente.
- Cliente: Recebe e exibe o estado atualizado do campo.

5. Final do Jogo:
- Servidor: Quando o cliente atinge o limite de tentativas ou afunda todos os navios, envia mensagem de fim de jogo e o estado final do campo.
- Cliente: Recebe e exibe a mensagem de fim de jogo.

6. Desconexão:
- Servidor e Cliente: Fecham a conexão quando o jogo termina ou o cliente opta por sair.

## Mensagens Trocadas
1. Mensagem de Boas-Vindas:
- Servidor para Cliente: "\nBem-vindo ao jogo Batalha Naval!\n"

2. Jogada do Cliente:
- Cliente para Servidor: "<letra> <número>\n"
- Servidor para Cliente: Confirmação da jogada e resultado (acerto/erro), seguido do estado atualizado do campo.

3. Mensagem de Erro:
- Servidor para Cliente: Em caso de coordenadas inválidas ou repetidas, uma mensagem específica é enviada para o cliente corrigir a entrada.

4. Mensagem de Fim de Jogo:
- Servidor para Cliente: "\nFim de jogo!\n"
 
## Estrutura do Protocolo (resumo)
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

### Funcionamento do Jogo (resumo)

- Cada jogador tem 20 tentativas para acertar os navios do adversário.
- O tabuleiro é de 15x15 e contém 10 navios posicionados aleatoriamente.
- O servidor gerencia o estado do jogo e o tabuleiro para cada cliente conectado.

## Funcionamento do Software

## Servidor
1. Inicialização:
- Cria um socket TCP/IP.
- Vincula o socket a um endereço IP e porta.
- Escuta conexões de entrada.

2. Gerenciamento de Conexões:
- Aceita novas conexões e cria uma nova thread para cada cliente.
- Envia mensagem de boas-vindas ao cliente.

3. Gerenciamento do Jogo:
- Inicializa o campo de batalha e posiciona os navios.
- Recebe jogadas do cliente, processa a jogada e envia o resultado.
- Mantém o controle do número de tentativas e acertos do cliente.
- Envia mensagem de fim de jogo quando aplicável.

4. Desconexão:
- Fecha a conexão com o cliente ao final do jogo ou por comando do cliente.

## Cliente

1. Inicialização:
- Cria um socket TCP/IP.
- Conecta-se ao servidor.

2. Interação com o Servidor:
- Recebe a mensagem de boas-vindas.
- Envia jogadas ao servidor e recebe o resultado.
- Exibe o estado atualizado do campo e o número de tentativas.

3. Desconexão:
- Fecha a conexão ao final do jogo ou por comando do usuário.



### Colaboradores
- Brenda `Brendacas`
- Flávia `fasjesus`
- Isaac `inlima`
- Laiz `laizcruz`
