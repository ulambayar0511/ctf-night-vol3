import socket


host = 'localhost'
port = 10000
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
answer = s.recv(size)
a = int(s.recv(size))
print(a)
result = int(a * (a + 1) * (2 * a + 1) / 6)
s.send(str(result).encode())
print(s.recv(size).decode())
s.close()
