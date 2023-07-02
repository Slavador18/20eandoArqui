# Ejemplo básico del echo server

import socket
SOCK_BUFFER = 1024


if __name__ == '__main__':
    # Este código se copia y pega siempre
    server_address = ('localhost', 5000)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f"Iniciando el servidor en la direccion {server_address[0]} y puerto {server_address[1]}")
    sock.bind(server_address)
    sock.listen(1)

    # Bucle de servidor
    while True:
        print("Esperando conexiones...")
        try:
            client_socket, client_address = sock.accept()
            print(f"Conexion desde {client_address[0]} en puerto {client_address[1]}")

            try:
                while True:
                    # Recibir data
                    data = client_socket.recv(SOCK_BUFFER)
                    print(f"Recibí: {data}")
                    
                    # Enviar data
                    if data:
                        print("Enviando data")
                        client_socket.sendall(data)
                    else:
                        break

            except ConnectionResetError:
                print("El cliente cerró la conexión")
            finally:
                print("Cerrando conexión")
                client_socket.close()
        except KeyboardInterrupt:
            print("El usuario terminó el programa")
            break

        


