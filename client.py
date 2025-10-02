import socket

HOST = "192.168.1.100"  # IP del Raspberry Pi
PORT = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

while True:
    comando = input("Inserisci comando (forward/backward/left/right/stop): ")
    client_socket.sendall(comando.encode("utf-8"))
    if comando == "exit":
        break

client_socket.close()