import socket


def main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.bind((host, port))

    s.listen(1)
    c, addr = s.accept()

    print("Connestion from: " + str(addr))
    while True:
        data = c.recv(1024).decode('utf-8')
        if not data:
                break
        print("From connected user: " + data)
        print("Message received " + data)
        c.send(data.encode('utf-8'))
    c.close()


if __name__ == '__main__':
        main()
