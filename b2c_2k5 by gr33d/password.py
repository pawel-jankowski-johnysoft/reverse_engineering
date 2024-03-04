import sys

EXPECTED_SUM_FROM_LOGIN = 0xc390
CONST_LOGIN_GENERATING_MAGIC = 0x400

EXPECTED_SUM_OTHER_PASSWORD_PART = 0x0285
OTHER_PASSWORD_PART_MINUS_SPLITTED_SUM = EXPECTED_SUM_OTHER_PASSWORD_PART - 0xc3 -0x90

OTHER_PASSWORD_PART_FIRST_XOR = 0x6433
OTHER_PASSWORD_PART_SECOND_XOR = 0x2456


def lower_short_password():
  # higher 8 bits -> generated number, 8 lower bits -> 0x0285 - 0xc3 - 0x90 - 0xFF
  number_before_hash = (0xFF << 8) | (OTHER_PASSWORD_PART_MINUS_SPLITTED_SUM - 0xFF)
  
  # xors used in algorithm -> addresses 0x4012FF in crackme
  return number_before_hash ^ OTHER_PASSWORD_PART_FIRST_XOR ^ OTHER_PASSWORD_PART_SECOND_XOR

def generate_password(login):
  login_hash = EXPECTED_SUM_FROM_LOGIN + CONST_LOGIN_GENERATING_MAGIC

  # expected sum needs to be substracted by char value - 1
  for char in str.encode(login):
    login_hash -= (char-1)


  #Login hash makes older 16 bits in result, then combine them with lower 16 bits
  #finally printed whole number as hex value
  print(hex((login_hash << 16) | lower_short_password()))


if __name__ == '__main__':
  if len(sys.argv) <2:
    sys.exit('use: python3 password.py <login>')

  generate_password(sys.argv[1])
