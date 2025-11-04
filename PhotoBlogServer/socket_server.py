import socket
from datetime import datetime

HOST = '127.0.0.1'
PORT = 8000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f'Listening on {HOST}:{PORT}')
    conn, addr = s.accept()
    with conn:
        print(f'Connected by {addr}')
        data = conn.recv(4096)
        if data:
            print(data.decode('utf-8', errors='ignore'))
            timestamp = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
            filename = f'request_{timestamp}.bin'
            with open(filename, 'wb') as f:
                f.write(data)
            print(f'Saved to {filename}')
