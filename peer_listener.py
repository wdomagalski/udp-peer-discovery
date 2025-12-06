import socket

PORT = 50050
MSG = b"DISCOVER"
REPLY = b"HELLO"

def run():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("", PORT))

    print("Peer listener running...")

    while True:
        data, addr = s.recvfrom(1024)
        if data == MSG:
            s.sendto(REPLY, addr)

if __name__ == "__main__":
    run()