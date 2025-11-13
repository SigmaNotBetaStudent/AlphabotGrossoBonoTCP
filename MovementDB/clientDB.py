import socket
from pynput import keyboard
import sqlite3 as sql
import time

SERVER_ADDRESS = ("192.168.1.127", 5000) # Indirizzo IP del server al quale mando un messaggio e sua porta

# Crea un socket IPv4 UDP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # STREAM = TCP
s.connect(SERVER_ADDRESS)

def leggi_comandi(nome, carattere):
    con = sql.connect(nome)
    cur = con.cursor()
    sequenza_file = cur.execute(f"SELECT Mov_Com FROM MOVEMENTS WHERE Tasto = ?", (carattere, )) # WHERE val = '{x}'
    sequenza = sequenza_file.fetchall()
    singole_istruzioni = sequenza[0][0].split(",")

    for i in range(0, len(singole_istruzioni), 2):
        istruzione = "DB" + singole_istruzioni[i]
        tempo = float(singole_istruzioni[i + 1])
        print(f"{istruzione}")
        s.send(istruzione.encode())
        time.sleep(tempo)
        s.send("stop".encode())
        
    con.close()

def on_press(key):
    try:
        if key.char == "w":
            s.send("w".encode())
        elif key.char == "a":
            s.send("a".encode())
        elif key.char == "s":
            s.send("s".encode())
        elif key.char == "d":
            s.send("d".encode())
        else:
            leggi_comandi("alphabotMoves.db", key.char)
    except AttributeError:
        if key == keyboard.Key.up:
            s.send("w".encode())
        elif key == keyboard.Key.left:
            s.send("a".encode())
        elif key == keyboard.Key.down:
            s.send("s".encode())
        elif key == keyboard.Key.right:
            s.send("d".encode())
        elif key == keyboard.Key.esc:
            s.send("finish".encode())
            s.close()
            return False

def on_release(key):
    s.send("stop".encode())

with keyboard.Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()