import socket
import json
from _thread import *

connection = True


def client_thread(conn, addr):
    global userMap
    username = conn.recv(1024)
    if username:
        username = username.decode("utf8")
    print(f"----------Connected by {username}----------")
    try:
        while True:
            msg = conn.recv(1024)
            if not msg:
                break
            message = msg.decode("utf8")
            if message == "exit":
                print(f"----------{username} disconnected----------")
                return
            else:
                print(f"[{username}]: {message}")
                conn.sendall(msg)
    except:
        print("error")
        pass


def main():
    with open("config.json") as json_config:
        data = json.load(json_config)

    server = data["server"]
    HOST = server["HOST"]    # The server's hostname or IP address
    PORT = server["PORT"]        # The port used by the server

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen()
    print("server start listening")
    while connection:
        conn, addr = s.accept()
        start_new_thread(client_thread, (conn, addr))

    s.close()


if __name__ == "__main__":
    main()
