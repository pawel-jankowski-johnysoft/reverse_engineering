

code_instructions_used_to_xor_with_login = bytearray.fromhex('83C20E891DF0304000538D1D5F3040008B0B5B83EB3833C0EB0A8B0333C1890383C3044A0BD275F233C9F7E18D3D8730')
login = 'JohnTheBest'
login_as_bytes = login.encode('ascii')

login_xored = bytearray()

for i in range(0, 8):
    magic_part = code_instructions_used_to_xor_with_login[i:i + 4]
    magic_part.reverse()

    login_part = bytearray(login_as_bytes[i:i + 4])
    if(len(login_part) < 4):
        for _ in range(4 - len(login_part)):
            login_part.append(0)
    login_part.reverse()
    result = bytearray()
    for a, b in zip(magic_part, login_part):
        result.append(int(a ^ b) & 0xff)

    result.reverse()
    for char in result:
        login_xored.append(char)

xlat_table = bytearray('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+'.encode() + login_as_bytes)
edx = len(login_as_bytes)
ax = 0
esi = 0
password = bytearray()
while edx >= 0:
    ax = ax & 0x00ff
    ecx = 6
    while ecx !=0:
        edx-=1
        if edx < 0:
            break
        ax = (ax & 0xFF00) | (login_xored[esi] & 0xff)
        esi = esi + 1
        ax = ax << ecx
        ah = (ax & 0xff00) >> 8
        al = ax & 0xFF
        ah = xlat_table[ah]
        password.append(ah)
        al = al >> ecx
        ax = (al << 8) | ah
        ecx = ecx - 2
        if ecx == 0:
            ah = al
            ax = al << 8 | al
            password.append(xlat_table[al])




print(f"{login} / {password[0:8].decode('ascii')}")


