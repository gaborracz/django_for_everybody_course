import urllib.request

fileHandler = urllib.request.urlopen('http://127.0.0.1:9000/romeo.txt')

for line in fileHandler:
    print(line.decode().strip())