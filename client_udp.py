import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    while True:
        
        msgem = input("Digite a mensagem aqui ...")
        client.sendto(msgem.encode(), ("host", 8080))
        data, sender = client.recvfrom(1024)
        print(sender[0] + ":" + data.decode())

        if msgem.encode ==  "SAIR".strip() or sender == "SAIR".strip():
            break
            
except Exception as erro:
    print("Alguma coisa está errada: " , erro)

finally:
    client.close()
    