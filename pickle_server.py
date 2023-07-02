import socket
import pickle

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 5000)
    sock.bind(server_address)
    sock.listen(1)

    print("Esperando conexiones...")
    client_socket, client_address = sock.accept()

    data = client_socket.recv(1024)
    # Pickle puede recibir cualquier tipo de dato y empaquetarlo correctamente
    matriz1 = pickle.loads(data) # Recibe el dato
    print("Matriz recibida 1: ", matriz1)

    data = client_socket.recv(1024)
    matriz2 = pickle.loads(data)
    print("Matriz recibida 2: ", matriz2)

    client_socket.sendall(pickle.dumps(matriz1+matriz2))

    client_socket.close()
    sock.close()
