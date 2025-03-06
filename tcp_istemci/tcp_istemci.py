import socket
import zlib  # Sa�lama hesaplamak i�in

def calculate_checksum(data):
    """Verinin checksum'unu hesaplar."""
    return zlib.crc32(data) & 0xffffffff

# Soket olu�turma
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

# G�nderilecek veri
message = 'Merhaba, TCP sunucu!'.encode()
checksum = calculate_checksum(message)

# Veri ve sa�lamay� birle�tirerek bildirme
data_to_send = message + checksum.to_bytes(4, byteorder='big')
client_socket.sendall(data_to_send)

client_socket.close()
