import socket
from threading import Thread

# Konfigurasi server
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5002
separator_token = "<SEP>"

# Simpan semua socket client
client_sockets = set()

# Buat TCP socket
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((SERVER_HOST, SERVER_PORT))
s.listen(5)

print(f"[*] Server listening as {SERVER_HOST}:{SERVER_PORT}")

# Fungsi untuk mendengarkan pesan dari client
def listen_for_client(cs):
    while True:
        try:
            msg = cs.recv(1024).decode()
        except Exception as e:
            print(f"[!] Client disconnected: {e}")
            client_sockets.remove(cs)
            cs.close()
            break
        else:
            # Kirim ke semua client lain
            for client in client_sockets:
                if client != cs:
                    try:
                        client.send(msg.encode())
                    except Exception as e:
                        print(f"[!] Error sending message: {e}")

# Loop untuk menerima client baru
while True:
    client_socket, client_address = s.accept()
    print(f"[+] {client_address} connected.")
    client_sockets.add(client_socket)
    t = Thread(target=listen_for_client, args=(client_socket,))
    t.start()
