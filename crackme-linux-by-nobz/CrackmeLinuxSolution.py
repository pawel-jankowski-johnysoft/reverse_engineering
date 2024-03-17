
magic = b'\xbe\xba\x37\x13'

hashed_password = [-114, -40, 81, 102, -117, -39, 3, 103, -115, -2, 10, 62, -31, -105, 21]

hashed_password_as_positive_bytes = bytearray(map(lambda x: x & 0xff, hashed_password))

result = ''

for i in range(0, len(hashed_password_as_positive_bytes), 4):
    for a, b in zip(hashed_password_as_positive_bytes[i:i + 4], magic):
        result += chr(a ^ b)

print(result)
