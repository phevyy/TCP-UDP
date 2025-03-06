import socket
import zlib  # Sa�lama hesaplamak i�in

def calculate_checksum(data):
    """Verinin checksum'unu hesaplar."""
    return zlib.crc32(data) & 0xffffffff

# Sunucu soketi olu�turma
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 12345))
print("UDP Sunucu dinleniyor...")

while True:
    data, addr = server_socket.recvfrom(1024)
    message, received_checksum = data[:-4], data[-4:]

    # Sa�lama kontrol�
    calculated_checksum = calculate_checksum(message)

    if calculated_checksum == int.from_bytes(received_checksum, byteorder='big'):
        print(f"Alinan veri: {message.decode()} - Checksum dogruland�.")
    else:
        print("Veri hatali! Checksum uyu�muyor.")
