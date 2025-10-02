import socket

HOST = "192.168.1.109"  # alphabot ip
PORT = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

print("Controllo robot. Comandi:")
print("f = avanti, b = indietro, l = sinistra, r = destra, s = stop")
print("Scrivi 'exit' per uscire.")

while True:
    comando = input("Inserisci comando (f/b/l/r/s): ").strip()
    if comando == "exit":
        break
    
    durata = input("Inserisci durata in secondi (es. 2.5): ").strip()
    
    # Se non metti durata, mando 0
    if durata == "":
        durata = "0"
    
    messaggio = f"{comando},{durata}"
    s.sendall(messaggio.encode("utf-8"))

s.close()
