; nasm -f elf32 -o 1.o 1.asm
; ld -m elf_i386 -o app 1.o
; ./app <login>

section .data
new_line db 0xA,0xC,0
pass_size db 1
password times 100 db 0

cracked times 100 db 0

section .text
global _start

_start:
        cmp dword [esp], 2
        jne koniec
        cld
        mov eax, 0
        mov esi, dword [esp + 8]
        mov edi, password
        mov ecx, -1
copy_to_password:
        inc ecx
        movsb
        cmp byte [edi-1], 0
        jne copy_to_password

        mov byte [pass_size], cl
        movzx edx, byte [pass_size]


crack:
        movzx edi, byte [pass_size]
        xor ecx, ecx
        mov edx, 'a'
        mov esi, password
_crack:
        xor ax, ax
        lodsb
        add al, 1
        add ah, dl
        mov word [cracked+2*ecx], ax
        inc dl
        inc ecx
        cmp ecx, edi
        jne _crack
print_pass:
        mov eax, 4
        mov ebx, 1
        mov ecx, cracked
        mov edx, edi
        add edx, edx
        int 0x80
print_new_line:
        mov eax, 4
        mov ebx, 1
        mov ecx, new_line
        mov edx, 2
        int 0x80
koniec:
        mov eax, 1
        mov ebx, 0
        int 80h
