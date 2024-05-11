
# tropes_safe_cracker_1 by trope
### https://crackmes.one/crackme/5ab77f6533c5d40ad448cb87

Simple crackme, static, six numbers code to break.

It's important to find function where code comparing is done. I set breakpoint on "lstrlen" function, then try "open" safe.
After catch breakpoint, latest address on stack is the one, which points checking function. 
First, algorithm checks length of password, then checks "randomly" each of 6 numbers. 
 `[edi + 0] [edi + 1]  [+2] [+3] [+4] [+5] [+6] [+7] [+8] [+9]`
`     [1]       [2]     [3] [4]  [5]  [6]  [7] [8]  [9]   [0]`

```[edi + 4 +2 - 3] [edi +2] [edi + 4] [edi + 4] [edi] [edi + 2] ```

Finally password is: 
``` [4] [3] [5] [5] [1] [3]```
