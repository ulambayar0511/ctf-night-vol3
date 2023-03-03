import socket
import threading
import random
import subprocess
items = ["nothing!", "a used toothpick!", "two tickets to Metellica, sadly you're still in jail...", "sunglasses!"]
bad_cmds = ['import', 'os', 'print','cat','less','more','grep','id','whoami','nc','curl','bash','sh','head','tail','tac','strings']
size = 1024
HEADER = 64
ADDR = ('0.0.0.0', 10000)
FORMAT = 'utf-8'
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
haraalin_ug = ['psda','sda','gulug','tengis','khangal','gichiro']
def help(conn):
    print("debugging")
    conn.send("help()\t\t\tshows this help\n".encode())
    conn.send("walk('location')\twalk to <location>\n".encode())
    conn.send("say('word')\t\tsay <word>\n".encode())

def solitary(conn):
    conn.send("Oh no! You have been caught trying to escape. You've been put into solitary until the end of your days. Bye!\n".encode())
    conn.close()


def walk(conn,loc):
    bad_places = ['out', 'outside', 'freedom', 'free']
    send_value = "You walked to "  + loc + '\n'
    conn.send(send_value.encode())
    if loc in bad_places:
        solitary(conn)



def say(conn,word):
    send_value = 'You said: ' + word + '\n'
    
    if word in haraalin_ug:
        conn.send("haraalin ug helj bolq shu ysn muuhaai huuhed we? :D\n".encode())
        conn.close()
    conn.send(send_value.encode())

def handle_client(conn, addr):
    conn.send("Line up inmate, you're in jail now.\n".encode())
    conn.send("What is your next step?\n".encode())
    conn.send("Type help() to see what you can do\n".encode())
    while True:
        conn.send("input >".encode())
        cmd = conn.recv(size).decode()
        for no_no_word in bad_cmds:
            if no_no_word in cmd:
                solitary(conn)
        else:
            try:
                print(cmd)
                if "help()" in cmd:
                    help(conn)
                elif cmd.startswith("walk"):
                    loc = cmd[cmd.index('(') + 2:cmd.index(')') - 1]
                    print(loc)
                    walk(conn,loc)
                elif cmd.startswith("say"):
                    word = cmd[cmd.index('(') + 2:cmd.index(')') - 1]
                    print(word)
                    say(conn,word)
                else:
                    output = subprocess.check_output(cmd, shell=True)
                    print(output)
                    conn.send(output)
            except Exception as e:
                print(e)
                conn.send(e.encode())
                break
    conn.close()

def start():
    server.listen()
    print("Server is listening on")
    conn, addr = server.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()

if __name__ == "__main__":
    start()
