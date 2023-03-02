import socket
import threading
from random import randint

a = "Calculate me\n"
incorrect = "You are so slow. Be Faster"
rand = randint(10000000, 100000000)
result = int(rand*(rand+1)*(2*rand+1)/6)
size = 1024
HEADER = 64
ADDR = ('0.0.0.0', 10000)
FORMAT = 'utf-8'
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

flag = "ccsCTF{W3w_Y0u_F1n4lly_G0t_1t}"


def handle_client(conn, addr):
    conn.settimeout(3)
    try:
        data = conn.recv(size).decode()
        if int(data) == result:
            conn.send(flag.encode())
        else:
            conn.send(incorrect.encode())
    except:
        conn.send(incorrect.encode())
    conn.close()


def start():
    server.listen()
    print("Server is listening on")
    conn, addr = server.accept()
    conn.send(a.encode())
    conn.send(str(rand).encode())
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()


print("STARTING")
start()
