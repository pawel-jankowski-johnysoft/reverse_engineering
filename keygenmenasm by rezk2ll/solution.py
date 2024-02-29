import sys

def generate_password(login):
    password = ''
    salt = 5
    for char in login:
        password += chr(ord(char) | salt)
        salt = ord(char)

    return password

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('Usage: python3 solution.py <login>')
    print(generate_password(sys.argv[1]))
