import socket
from AlphaBot import AlphaBot

# Inizializza il robot
bot = AlphaBot()

HOST = "0.0.0.0"  # Ascolta su tutti gli IP del Raspberry
PORT = 5000       # Porta TCP (scegli tu, >1024)

# Crea socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"Server in ascolto su {HOST}:{PORT}")

while True:
    conn, addr = server_socket.accept()
    print(f"Connessione da {addr}")
    
    while True:
        data = conn.recv(1024).decode("utf-8").strip()
        if not data:
            break

        print(f"Comando ricevuto: {data}")

        if data == "forward":
            bot.forward()
        elif data == "backward":
            bot.backward()
        elif data == "left":
            bot.left()
        elif data == "right":
            bot.right()
        elif data == "stop":
            bot.stop()
        else:
            print("Comando non riconosciuto")
    
    conn.close()
