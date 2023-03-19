#
# The world simplest web browser.
#
 
import socket
import sys

mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySock.connect(('data.pr4e.org', 80))
command = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode()
mySock.send(command)

while True:
    data = mySock.recv(512)
    
    if len(data) < 1:
        print("There was no incoming data...")
        sys.exit(1)
    
    print(data.decode(), end="")

    mySock.close()
    sys.exit(0)