# 5iriu5's SSE Login

### https://crackmes.one/crackme/65a81968eef082e477ff5d10

Crackme with "hard coded", encrypted login & password. Archive contains 2 versions: easy & harder.
To break "harder" one, you have to find entrypoint ("readelf -f" will be helpful with that)
Crackme uses SIMD (Single Instruction, Multiple Data) instructions (from SSE/SSE2), this is biggest difficulty.

Password for crackme: **crackmes.one**

Hint: 
To reverse encoded login / pass, set breakpoint at: 0x401078, a few instructions there allows to decode login / pass
