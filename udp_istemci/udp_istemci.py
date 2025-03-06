import socket
import zlib  # Checksum hesaplamak için

def calculate_checksum(data):
    """Verinin checksum'unu hesaplar."""
    return zlib.crc32(data) & 0xffffffff

#  Soketi oluþturma
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Gönderilecek veri
message = 'Merhaba, UDP sunucu!'.encode()
checksum = calculate_checksum(message)

# Veri ve saðlamayý birleþtirerek gönderme
data_to_send = message + checksum.to_bytes(4, byteorder='big')
client_socket.sendto(data_to_send, ('localhost', 12345))

client_socket.close()
