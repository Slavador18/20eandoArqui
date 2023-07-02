import socket
SOCK_BUFFER = 1024

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 5000)
    
    print(f"Conectando a {server_address[0]}: {server_address[1]}")
    sock.connect(server_address)
    try:
        msg = "Hola Mundo"
        sock.sendall(msg.encode())
        data = sock.recv(SOCK_BUFFER)
    
    finally:
        print("Cerrando conexión")
        sock.close()