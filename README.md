# simple-client-udp

Cliente UDP simples
Este código é um cliente UDP simples que envia uma mensagem para um servidor e recebe uma resposta.

Instalação
Para instalar o código, você precisa ter Python instalado em seu computador. Depois de instalar o Python, você pode baixar o código do GitHub.

git clone https://github.com/[Seu nome de usuário]/udp-client.git
Execução
Para executar o código, você precisa abrir um terminal e navegar até o diretório onde o código foi baixado. Em seguida, execute o seguinte comando:

python3 client.py
Exemplos
Aqui estão alguns exemplos de como usar o código:

# Enviar uma mensagem

mensagem = "Olá, mundo!"

client.sendto(mensagem.encode(), ("host", 8080))

# Receber uma resposta

data, sender = client.recvfrom(1024)

print(sender[0] + ":" + data.decode())


Licença
Este código é licenciado sob a licença MIT.
