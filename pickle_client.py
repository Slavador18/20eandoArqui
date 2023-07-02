import socket
import pickle

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 5000)
    sock.connect(server_address)

    try:
        matriz1 = [[1, 2], [3, 4]]
        matriz2 = [[4, 3], [2, 1]]
        
        # Envío de matriz 1
        # Se debe serializar antes de enviar
        serialized_data = pickle.dumps(matriz1) 
        sock.sendall(serialized_data) # Envia data

        # Envío de matriz 2
        serialized_data = pickle.dumps(matriz2)
        sock.sendall(serialized_data)

        #print("Matrices enviadas")
        # Recibe el resultado
        data_received = sock.recv(1024) # Recibe
        producto = pickle.loads(data_received) # Lo carga con pickles 
        print(f"Producto de las matrices:\n{producto}")

    finally:
        # Cierro la conexión
        #print("Cerrando conexión")
        sock.close()