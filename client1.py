import socket

mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySock.connect(("127.0.0.1", 9000))
command = "GET http://127.0.0.1:9000/romeo.txt HTTP/1.0\r\n".encode()
mySock.send(command)

while True:
    data = mySock.recv(512)
    if len(data) < 1: break
    print(data.decode(), end="")

mySock.close()