import sqlite3
from pynput import keyboard

def on_press(key):
    try:
        print(key)
        x = key.char
        con = sqlite3.connect('./movementsDB.db')
        cur = con.cursor()
        res = cur.execute(f"SELECT command FROM Movements WHERE key = '{x}'")
        results = res.fetchall()
        con.close()
        if results:
            results = [item[0] for item in results][0]
            print(results.replace(' ', '').split('|'))
        else:
            print(f"Nessun comando trovato per il tasto '{x}'")
    except Exception as e:
        print(f"Errore: {e}")

def on_release(key):
    pass

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
