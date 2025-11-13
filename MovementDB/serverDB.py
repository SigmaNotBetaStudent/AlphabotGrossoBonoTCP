import socket
from AlphaBot import AlphaBot

# Inizializza il robot
bot = AlphaBot()

HOST = "0.0.0.0"
PORT = 5000

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

        if data == "w":
            bot.forward()
        elif data == "a":
            bot.left()
        elif data == "s":
            bot.backward()
        elif data == "d":
            bot.right()
        elif data == "stop":
            bot.stop()
        elif data == "finish":
            bot.stop()  # Assicurati che il robot si fermi prima di chiudere
            conn.close()
            break
        elif data.startswith("DB"):
            # Estrai il comando dopo "DB"
            cmd = data[2:]  # Rimuovi "DB" dal comando
            if cmd == "f":
                bot.forward()
            elif cmd == "b":
                bot.backward()
            elif cmd == "l":
                bot.left()
            elif cmd == "r":
                bot.right()
            else:
                print(f"Comando DB non riconosciuto: {cmd}")
        else:
            print(f"Comando non riconosciuto: {data}")
    
    # Chiudi la connessione se non già chiusa
    try:
        conn.close()
    except:
        pass
