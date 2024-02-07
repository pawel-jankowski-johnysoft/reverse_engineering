PARAM=${1}
nasm -f elf32 -o 1.o crackme.asm
ld -m elf_i386 -o 1 1.o
./1 $PARAM
