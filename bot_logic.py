import random
import time

def gen_pass(pass_length):
    character = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    
    password = ""

    for i in range (pass_length):
        password += random.choice(character)

    return password

def coins(detik):
    face = random.randint(1,2)
    if face == 1:
        time.sleep(detik)
        return 'koin atas'
    else:
        time.sleep(detik)
        return 'koin bawah'
