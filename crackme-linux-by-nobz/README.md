# Crackme-linux by nobz
### https://crackmes.one/crackme/5ab77f5833c5d40ad448c3d2 
#### x86 kernel calls https://gist.github.com/GabriOliv/a9411fa771a1e5d94105cb05cbaebd21
Interesting and difficult crackme. One anti-debug technique has been applied - system call 0x1A uses ptrace to check if debbuger has been attached.
Another difficulties are "instructions inside instructions" - instructions shown using "x/10i $pc" are different than executed in code - some calls do jumps
to code "between instructions", eg (abstraction example, only focused on to show, how code analyze might be strange)

```
mov dword ptr [esp+4], eax
mov dword ptr [esp], ebx
call 0x00000600
0x00000400 mov eax, ebx
0x00000405 inc eax
...

0x00000600 push ebp
mov ebp, esp
...
mov eax, 1
dec eax
je 0x00000402
```
In this case list instructions under 0x00000402 will be totally different than looking on code at the beginning.

The security is quite simple - "hard coded" password xored using "0x1337babe". 

I decided to attach my notes - they are not "true" in many cases, but allows me simplify break password and understand, how code works.
