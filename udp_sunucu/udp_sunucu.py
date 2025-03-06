import socket
import zlib  # Saðlama hesaplamak için

def calculate_checksum(data):
    """Verinin checksum'unu hesaplar."""
    return zlib.crc32(data) & 0xffffffff

# Sunucu soketi oluþturma
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 12345))
print("UDP Sunucu dinleniyor...")

while True:
    data, addr = server_socket.recvfrom(1024)
    message, received_checksum = data[:-4], data[-4:]

    # Saðlama kontrolü
    calculated_checksum = calculate_checksum(message)

    if calculated_checksum == int.from_bytes(received_checksum, byteorder='big'):
        print(f"Alinan veri: {message.decode()} - Checksum dogrulandý.")
    else:
        print("Veri hatali! Checksum uyuþmuyor.")
