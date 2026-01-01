import socket
import time

PORT = 50050
MSG = b"DISCOVER"
REPLY = b"HELLO"

def discover(timeout=2):
    peers = []

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.settimeout(timeout)

    s.sendto(MSG, ("255.255.255.255", PORT))

    start = time.time()
    while time.time() - start < timeout:
        try:
            data, addr = s.recvfrom(1024)
            if data == REPLY:
                peers.append(addr[0])
        except socket.timeout:
            continue
        except Exception:
            pass

    s.close()
    return peers

if __name__ == "__main__":
    print("Looking for peers...")
    found = discover()
    print("Found:", found if found else "none")
