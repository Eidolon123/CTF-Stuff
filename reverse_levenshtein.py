import requests
import string
import re

alphalist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '"', '£', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '{', '}', '[', ']', '~', '@', ':', ';', "'", '#', '<', '>', '?', ',', '.', '/', '|', '\\', '`']
payload = {'flag': ''}  # Data
success_pos = []  # Positions of successfully guessed characters, means we can skip them on successive runs to reduce runtime
prev_num = 28  # Setting as 28 as this was the starting distance from the flag for this challenge
start = '****************************'  # Starting the program with the correct amount of characters to get closest score possible
number = 28
insert_string = ''
for char in alphalist:
    for i in range(len(start)):
        if i not in success_pos:  # If we havent guessed this character correctly already
            new_string = start[:i] + char + start[i+1:]  # Insert current character guess in correct position
            payload['flag'] = f"spbctf{{{new_string}}}"  # Set up payload
            r = requests.post('https://cat-step.disasm.me/', data=payload)
            response = re.sub('\D', '', r.text)  # Strip response from site to just the levenshtein distance from the flag
            if response != '':  # Make sure we dont hang on responses that dont give us a distance
                number = int(response)
            else:
                continue
            if number < prev_num:  # This indicates that the current guess is correct
                start = new_string
                success_pos.append(i)
            else:
                continue
            print(new_string)  # Print string with correct guess

            prev_num = number  # Store current levenshtein distance to check against on next loop through
        else:
            continue
