"""
CRC-8 calculation for 8 byte data frame

Polynomial: x^8 + x^2 + x + 1
            Bit Position    =   8   7   6   5   4   3   2   1   0
            Bit Value       =   1   0   0   0   0   0   1   1   1   =   0x07(8 bits polynomial)

eg data frame: [0x02, 0x04]

0x02
    [0]   0    0    0    0    0    0    0    0
    [0]   0    0    0    0    0    0    0    0
    [0]   0    0    0    0    0    0    0    0
    [0]   0    0    0    0    0    0    0    0
    [0]   0    0    0    0    0    0    0    0
    [0]   0    0    0    0    0    0    0    0
    [1]   0    0    0    0    0    1    1    1
    [0]   0    0    0    0    1    1    1    0

0x04
    [0]   0    0    0    1    1    1    0    0
    [0]   0    0    1    1    1    0    0    0
    [0]   0    1    1    1    0    0    0    0
    [0]   1    1    1    0    0    0    0    0
    [0]   1    1    0    0    0    1    1    1
    [1]   1    0    0    0    1    1    1    0
    [0]   0    0    0    1    1    0    1    1
    [0]   0    0    1    1    0    1    1    0

    CRC OUT = 0    0    1    1    0    1    1    0 = 54d = 0x36

"""

def reverse_bits(byte):
    result = 0
    for i in range(8):
        result = (result << 1) | (byte & 1)
        byte >>= 1
    return result


def CRC8(data_frame, polynomial):
    crc = 0x00
    for byte in data_frame:
        crc^=byte
        for _ in range(8):
            if (crc & 0x80):        #check if MSB bit is set (1000 0000b)
                crc = (crc<<1) ^ polynomial

            else:
                crc = crc<<1

            crc &=0xFF
    print(reverse_bits(crc))


data_frame = [0x02,0x04, 0x05, 0xAE]

for _ in range(len(data_frame)):
    data_frame[_] = reverse_bits(data_frame[_])

CRC8(data_frame,0x07)

