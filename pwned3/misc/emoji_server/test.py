# import time
# alphalist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '"', '£', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '{', '}', '[', ']', '~', '@', ':', ';', "'", '#', '<', '>', '?', ',', '.', '/', '|', '\\', '`']
# start = "******"
# goal = "fCt`sq"
# success_pos = []
# while len(success_pos) < 6:
#     for i in range(len(start)):
#         for char in alphalist:
#             print("Connection Open")
#             for i in range(len(start)):
#                 if i not in success_pos:
#                     new_string = start[:i] + char + start[i+1:]
#                     print(new_string)
#                     if new_string[i] == goal[i]:
#                         start = new_string
#                         success_pos.append(i)
#                     else:
#                         continue
#             print("Connection Closed")

# with open('/home/jamie/github/CTF-Stuff/pwned3/misc/emoji_server/words.txt', 'r') as f:
#     words = f.readlines()

# with open('/home/jamie/github/CTF-Stuff/pwned3/misc/emoji_server/words.txt', 'w') as f:
#     for word in words:
#         if word[0] == 'f':
#             f.write(word)
#         else:
#             continue

from pwn import *

# alphalist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '"', '£', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '{', '}', '[', ']', '~', '@', ':', ';', "'", '#', '<', '>', '?', ',', '.', '/', '|', '\\', '`']
word_list = list()
with open('/home/jamie/github/CTF-Stuff/pwned3/misc/emoji_server/words.txt', 'r') as f:
    for line in f.readlines():
        word_list += re.findall(r'\b(\w{6})\b', line)
closer = b'\xf0\x9f\xa5\xb5\n'
same = b'\xf0\x9f\x98\x90\n'
worse = b'\xf0\x9f\xa5\xb6\n'
for k in range(len(word_list)//12):
    conn = remote('157.245.28.90', 12000)
    for i in range(12):
        conn.sendline(f'pwned{{{word_list[i]}}}')
        response = conn.recvuntil(b'\n')
        if response not in [closer, same, worse]:
            print(response)
        if response == worse:
            with open('/home/jamie/github/CTF-Stuff/pwned3/misc/emoji_server/words.txt', 'w') as f:
                for number, line in enumerate(word_list):
                    if number != i:
                        f.write(f'{line}\n')
                    else:
                        continue
    conn.close()
