import socket
import zlib  # Saðlama hesaplamak için

def calculate_checksum(data):
    """Verinin checksum'unu hesaplar."""
    return zlib.crc32(data) & 0xffffffff

# Soket oluþturma
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

# Gönderilecek veri
message = 'Merhaba, TCP sunucu!'.encode()
checksum = calculate_checksum(message)

# Veri ve saðlamayý birleþtirerek bildirme
data_to_send = message + checksum.to_bytes(4, byteorder='big')
client_socket.sendall(data_to_send)

client_socket.close()
