
import sys
def crack(login):
    magic = ord('a')
    for current_char in login:
        print(chr(ord(current_char)+1) + chr(magic) , end='')
        magic += 1
    print()

if __name__ == '__main__':
    if len(sys.argv) < 2:
       sys.exit('Usage: %s <login>' % sys.argv[0])
    crack(sys.argv[1])
