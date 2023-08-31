import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


client.sendto(b'enviando alguma coias  .....', ("localhost", 8080))
data, sender = client.recvfrom(1024)
print (sender[0] + ":" + data.decode())

