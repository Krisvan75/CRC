"""
CRC-8 calculation for 8 byte data frame
"""

def CRC8(data_frame, polynomial):
    crc = 0x00
    for byte in data_frame:
        crc^=byte
        for _ in range(8):
            if (crc & 0x80):
                crc = (crc<<1) ^ polynomial

            else:
                crc = crc<<1

            crc &=0xFF
    print(crc)


data_frame = [0x01,0x02,0x03]

CRC8(data_frame,0x07)

