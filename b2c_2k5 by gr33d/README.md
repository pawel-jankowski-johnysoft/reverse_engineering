# b2c_2k5_1 by gr33d
### https://crackmes.one/crackme/5ab77f6133c5d40ad448c959

Description doesn't explain all steps in code, it is my interpretation simplified based on code 
Crackme's algorithm can be splitted into a few steps:
- make password upper case
- change "password as string" to "password as number"
- for 16 higher bits of password:
a) substruct 0x400
b) for each character add it's (hex value - 1)
d) After all calculations compare it to 0xC390

- for lower 16 bits:
a) expected value is 0x285
b) higher 16 bits is known - both bytes should be substructed from 0x285:
0x285 - 0xc3 - 0x90 = 0x132

Higher byte should be 0xFF (for other values comparing to 0x285 worked fine, but next call doesn't work - function clear EDI register)

Lower byte is equal to: 0x132 - 0xFF  = 0x33


now for bytes:
0xFF33
it is needed to do 2 xor operations (0x6433 & 0x2456)

Finally combine value created using login (as 16 higher bits) & lower 16 bits created recently and print it as hex.
