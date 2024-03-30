## frogger_crackme by macabre

### https://crackmes.one/crackme/5ab77f5a33c5d40ad448c4f7


Interesting crackme - "self modifying" code, which needs correct offsets to break it. 
High level algorithm:
 - calculate login chars sum, then square it
 - last byte of calculate number is important - more details soon
 - password consists from 2 parts separated by "-"
 - first part is const: **62** (this number defines offset to first update at the end of algorithm - value 0xE9 goes under (0x080483D8 + 62))
 - second part is calculated as: `0 - sum(all chars after "-" from password)`
 - finally, second byte to replace goes under (0x080483D8 + 63) - value is calculated as:
` (last byte of second password part calculated XOR last byte of square of sum from login chars)` and it MUST BE **0x1c**
 - **0x1c** is offset to jmp instruction, where congratulations are displayed

### Notes:
I decided to generate passwords using only a - z characters, but it is possible upper case letters or any other characters
