import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    while True:
        
        print("A seguir insira o host e a porta que deseja comincar")
        host , porta = input("Digite o host e a porta separado por espaço: ").split()
        
        msgem = input("Digite a mensagem aqui: ")
        client.sendto(msgem.encode(), (host , int (porta)))
        data, sender = client.recvfrom(1024)
        print(sender[0] + ":" + data.decode())

        if msgem.encode().strip() ==  "SAIR" or data.strip() == "SAIR":
            break
        elif not msgem:
            print("A mensagem Não Pode estar vazia")
            continue
            
except Exception as erro:
    print("Alguma coisa está errada: " , erro)

finally:
    client.close()
    