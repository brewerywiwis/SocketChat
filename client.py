import socket
import json
import atexit


def disconnect(username, socket):
    print("-----exit client's app-----")
    socket.sendall(str.encode("exit"))
    socket.close()


def main():
    with open("config.json") as json_config:
        data = json.load(json_config)

    server = data["server"]
    HOST = server["HOST"]    # The server's hostname or IP address
    PORT = server["PORT"]        # The port used by the server

    username = input("please enter name to using chat app: ")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.send(str.encode(username))
    atexit.register(disconnect, username=username, socket=s)

    while True:
        message = input(">")
        if (message == "exit"):
            break
        if message:
            s.sendall(str.encode(message))
            data = s.recv(1024)
            # print('Received', repr(data))


if __name__ == "__main__":
    main()
