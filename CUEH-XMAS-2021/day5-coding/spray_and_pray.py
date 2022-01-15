import requests
import json
import base64
import pycurl
import time
from pwn import log
from queue import Queue

work = Queue()
last_elf = int(time.time()) # Time that last elf was deployed (in seconds from 1970)
rate = 21 # Elf respawn timer
sniped = False
logging = log.progress('Hunting Santa. Attempts: ') # Progress bar from pwn setup
elves_deployed = 1


# Create elf movement commands as a json dictionary
elf = ("""
elf.move(0.8);
elf.throw(0.25,1);
elf.turn(4);
""")
elf_bytes = elf.encode('ascii')
elf_b64_bytes = base64.b64encode(elf_bytes)
elf_b64 = elf_b64_bytes.decode('ascii')
payload_python = {
    "name":"elfThrower", 
    "code":elf_b64
}

def deploy_elf():
    '''Deploys killer elf in game at URL'''
    payload_json = json.dumps(payload_python)
    headers = {'content-type': 'application/json'}
    logging.status(str(elves_deployed))
    r = requests.post('http://192.168.191.128:2512/elf', headers=headers, data=payload_json)

def confirm_kill():
    '''Checks for success message in content, ends program if santa is hit'''
    c = requests.get('http://192.168.191.128:2512')
    if 'splattered' in c.content.decode('utf-8'):
        print("Kill Confirmed, check this mess for the flag because im lazy")
        print(c.content.decode('utf-8'))
        quit()


# This is a lot of jank im not sure how it works
deploy_elf() # Initial elf
while True:
    next_job = confirm_kill()
    if sniped == False:
        work.put(next_job)
    else:
        time.sleep(.1)
    now = int(time.time())
    if now - last_elf > rate:
        last_elf = now
        elves_deployed = elves_deployed + 1
        deploy_elf()
        

        


