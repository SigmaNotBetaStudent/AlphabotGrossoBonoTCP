import socket
from pynput import keyboard

HOST = "192.168.1.100"  # 🔹 IP del Raspberry Pi (modifica con il tuo)
PORT = 5000

# Crea una connessione TCP con il server
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect((HOST, PORT))

def invia(comando):
    conn.sendall(comando.encode("utf-8"))
    print(f"Inviato comando: {comando}")

def premi(key):
    try:
        if key.char in ['w', 'a', 's', 'd']:
            if key.char == 'w':
                invia("f")   # avanti
            elif key.char == 's':
                invia("b")   # indietro
            elif key.char == 'a':
                invia("l")   # sinistra
            elif key.char == 'd':
                invia("r")   # destra
    except AttributeError:
        # Controlla tasti speciali
        if key == keyboard.Key.space:
            invia("s")  # stop

def rilascia(key):
    # Quando rilascio un tasto, fermo il robot
    if key.char in ['w', 'a', 's', 'd']:
        invia("s")
    elif key == keyboard.Key.esc:
        print("Chiusura connessione.")
        conn.close()
        return False  # ferma il listener

# Avvia l'ascoltatore
with keyboard.Listener(on_press=premi, on_release=rilascia) as listener:
    listener.join()
