# -*- coding: utf-8 -*-
import struct, zlib

def create_png(filename, width, height):
    pixels = []
    for y in range(height):
        row = [0]
        for x in range(width):
            r = int(102 + (118 - 102) * x / width)
            g = int(126 + (75 - 126) * x / width)
            b = int(234 + (162 - 234) * x / width)
            row.extend([r, g, b, 255])
        pixels.append(bytes(row))
    
    raw_data = b''.join(pixels)
    
    def make_chunk(chunk_type, data):
        chunk = chunk_type + data
        crc = struct.pack('>I', zlib.crc32(chunk) & 0xFFFFFFFF)
        return struct.pack('>I', len(data)) + chunk + crc
    
    png = b'\x89PNG\r\n\x1a\n'
    ihdr_data = struct.pack('>IIBBBBB', width, height, 8, 6, 0, 0, 0)
    png += make_chunk(b'IHDR', ihdr_data)
    compressed = zlib.compress(raw_data)
    png += make_chunk(b'IDAT', compressed)
    png += make_chunk(b'IEND', b'')
    
    with open(filename, 'wb') as f:
        f.write(png)
    print('Created: ' + filename)

create_png('icon-192.png', 192, 192)
create_png('icon-512.png', 512, 512)
print('Done!')
