import sys

def generate_password(input):
    rored_length = (len(input) >> 1)
    password = str(len(input))
    password += input[2]
    for single_char in input:
        password += chr(ord(single_char) + 1 + rored_length)
    return password


if __name__ =='__main__':
    if len(sys.argv) < 2:
        sys.exit('python3 solution.py <login>')
    print(generate_password(sys.argv[1]))
