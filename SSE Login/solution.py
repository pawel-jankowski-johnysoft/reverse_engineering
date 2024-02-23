hashed = bytearray.fromhex('42 75 84 a9 1a 75 83 d5 62 3e 8e 20 c5 fc f6 92')
salt = bytearray.fromhex('d2 09 23 42 a5 10 79 d5 fb cf 2a 16 c5 fc f6 92')

for pair in list(zip(hashed, salt)):
  result = (pair[0] - pair[1]) & 0xff
  print(chr(result), end='')
