# server_control.py
import socket
import time
from AlphaBot import AlphaBot  # Assicurati che AlphaBot sia in AlphaBot.py

bot = AlphaBot()

HOST = "0.0.0.0"
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"Server in ascolto su {HOST}:{PORT}")

conn, addr = server_socket.accept()
print(f"Connessione da {addr}")

try:
    while True:
        data = conn.recv(1024).decode().strip().lower()
        DR_sensor, DL_sensor = bot.sensor()
        if not data:
            continue

        print(f"{DR_sensor}")
        if data == 'w':
            bot.forward()
        elif data == 's':
            bot.backward()
        elif data == 'a':
            bot.left()
        elif data == 'd':
            bot.right()
        elif data == 'x':  # ferma il robot
            bot.stop()
        else:
            bot.stop()

        time.sleep(0.5)
        bot.stop()

except KeyboardInterrupt:
    bot.stop()
    import RPi.GPIO as GPIO
    GPIO.cleanup()
    conn.close()
    server_socket.close()
