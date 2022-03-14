from pwn import *
import time
alphalist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '"', '£', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '{', '}', '[', ']', '~', '@', ':', ';', "'", '#', '<', '>', '?', ',', '.', '/', '|', '\\', '`']
start = "******"
success_pos = []
closer = b'\xf0\x9f\xa5\xb5\n'
same = b'\xf0\x9f\x98\x90\n'
worse = b'\xf0\x9f\xa5\xb6\n'
while len(success_pos) < 6:
    for i in range(len(start)):
        for char in alphalist:
            conn = remote('157.245.28.90', 12000)
            conn.sendline('******')
            for i in range(len(start)):
                if i not in success_pos:
                    new_string = start[:i] + char + start[i+1:]
                    print(new_string)
                    time.sleep(0.1)
                    conn.sendline(f'{new_string}')
                    response = conn.recvuntil(b'\n')
                    if response == worse:
                        start = new_string
                        success_pos.append(i)
                    else:
                        continue
                else:
                    continue
            conn.close()