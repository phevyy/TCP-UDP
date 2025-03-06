import socket
import zlib  #  Saðlamasýný yapmak  için

def calculate_checksum(data):
    """Verinin checksum'unu hesaplar."""
    return zlib.crc32(data) & 0xffffffff

# Soket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(5)
print("TCP Sunucu dinleniyor...")

while True:
    client_socket, addr = server_socket.accept()
    print(f"Baglanti kuruldu: {addr}")

    # Veri
    data = client_socket.recv(1024)
    message, received_checksum = data[:-4], data[-4:]

    # Saðlama kontrolü
    calculated_checksum = calculate_checksum(message)

    if calculated_checksum == int.from_bytes(received_checksum, byteorder='big'):
        print(f"Alinan veri: {message.decode()} - Checksum dogrulandi.")
    else:
        print("Veri hatalý! Checksum uyusmuyor.")

    client_socket.close()
