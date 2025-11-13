import socket
import AlphaBot
import time

ADDRESS = ('0.0.0.0', 4004) # 0-0-0-0 : indirizzo speciale anche detto "this host" 
BUFFER = 4096

#crea un socekt ipv4 TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

alphabot = AlphaBot.AlphaBot()
alphabot.stop()

s.bind(ADDRESS)
s.listen(5)
#accetta connesione
conn, addr = s.accept()


try:
    while True:
        data_byte = conn.recv(BUFFER)
        instruction = data_byte.decode().strip()

        print(f"Received: {instruction}")

        if instruction == 'w':
            alphabot.setMotor()
        elif instruction == 'a':
            alphabot.left()
        elif instruction == 's':
            alphabot.setMotor()
        elif instruction == 'd':
            alphabot.right()
        elif instruction == 'stop':
            alphabot.stop()
        else:
            print("Unknown command")

        conn.send("ricevuto".encode())
        
except Exception as e :
    print(f"ERROR!: {e}" )
finally:
    s.close()