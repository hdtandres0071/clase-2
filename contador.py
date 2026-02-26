import socket
import threading

contador_clientes = 0  # recurso compartido
lock = threading.Lock()  # para proteger el contador

def handle_client(conn, addr):
    global contador_clientes

    try:
        name = conn.recv(1024).decode()

        # Proteger el recurso compartido
        with lock:
            contador_clientes += 1
            numero_cliente = contador_clientes

        print(f"Cliente {numero_cliente} atendido desde {addr}")

        response = f"Hola {name}, eres el cliente número {numero_cliente}"
        conn.sendall(response.encode())

    except Exception as e:
        print(f"Error con {addr}: {e}")

    finally:
        conn.close()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 5000))
server.listen()

print("Servidor concurrente con contador...")

while True:
    conn, addr = server.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()

