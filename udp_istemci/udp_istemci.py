import socket
import zlib  # Checksum hesaplamak i�in

def calculate_checksum(data):
    """Verinin checksum'unu hesaplar."""
    return zlib.crc32(data) & 0xffffffff

#  Soketi olu�turma
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# G�nderilecek veri
message = 'Merhaba, UDP sunucu!'.encode()
checksum = calculate_checksum(message)

# Veri ve sa�lamay� birle�tirerek g�nderme
data_to_send = message + checksum.to_bytes(4, byteorder='big')
client_socket.sendto(data_to_send, ('localhost', 12345))

client_socket.close()
