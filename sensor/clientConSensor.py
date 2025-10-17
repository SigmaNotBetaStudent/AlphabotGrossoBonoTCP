# client.py
import socket

HOST = "192.168.1.109"  # inserisci l'IP del Raspberry Pi
PORT = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
print("Connesso al robot. Usa WASD per muovere, X per fermare, Q per uscire.")

try:
    while True:
        cmd = input("Comando (W/A/S/D/X): ").strip().lower()
        if cmd == 'q':
            break
        client_socket.send(cmd.encode())

except KeyboardInterrupt:
    pass
finally:
    client_socket.close()
    print("Connessione chiusa.")
