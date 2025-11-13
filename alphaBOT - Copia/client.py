import socket
from pynput import keyboard
import sqlite3 as sql
import time

SERVER_ADDRESS = ("192.168.1.127", 4004)  # TCP server

# Crea un socket TCP
Client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Client.connect(SERVER_ADDRESS)

startTime = 0
keyPressed = ""

def leggi_comandi(db_name, carattere):
    """Legge i comandi dal database e li invia al server con tempistiche."""
    con = sql.connect(db_name)
    cur = con.cursor()
    sequenza_file = cur.execute("SELECT Mov_Com FROM MOVEMENTS WHERE Tasto = ?", (carattere,))
    sequenza = sequenza_file.fetchall()
    
    if sequenza:
        singole_istruzioni = sequenza[0][0].split(",")
        for i in range(0, len(singole_istruzioni), 2):
            istruzione = "DB" + singole_istruzioni[i]
            tempo = float(singole_istruzioni[i + 1])
            print(f"Invio: {istruzione}")
            Client.send(istruzione.encode())
            time.sleep(tempo)
            Client.send("stop".encode())
    
    con.close()

def on_press(key):
    global keyPressed, startTime
    try:
        # lettere principali
        if key.char in ['w', 'a', 's', 'd', 'q', 'c']:
            keyPressed = key.char
            startTime = time.time()
            Client.send(key.char.encode())
        else:
            # altre lettere leggono i comandi dal db
            leggi_comandi("alphabotMoves.db", key.char)
    except AttributeError:
        # tasti speciali
        if key == keyboard.Key.up:
            Client.send("w".encode())
        elif key == keyboard.Key.left:
            Client.send("a".encode())
        elif key == keyboard.Key.down:
            Client.send("s".encode())
        elif key == keyboard.Key.right:
            Client.send("d".encode())
        elif key == keyboard.Key.space:
            Client.send("stop".encode())
        elif key == keyboard.Key.esc:
            print("Exiting...")
            Client.send("finish".encode())
            return False

def on_release(key):
    global keyPressed
    keyPressed = ""
    try:
        Client.send("stop".encode())
    except:
        pass

try:
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
finally:
    Client.close()
