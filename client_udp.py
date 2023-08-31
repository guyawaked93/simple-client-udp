import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    while True:
        
        mensagem = client.sendto(input("Digite a mensagem aqui .... ").encode(), ("host", 8080))
        data, sender = client.recvfrom(1024)
        print(sender[0] + ":" + data.decode())

        if mensagem.encode ==  "SAIR\n" or sender == "SAIR\n":
            break    
            
except Exception as erro:
    print("Alguma coisa está errada: " , erro)

finally:
    client.close()
    