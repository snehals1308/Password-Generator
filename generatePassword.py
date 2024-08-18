import random
import string

def gen_password(min_length,num=True,special_char=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if num:
        characters += digits
    if special_char:
        characters += special

    pwd = ""
    criteria = False
    has_num = False
    has_special = False

    while not criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_num = True
        elif new_char in special:
            has_special = True

        criteria = True
        if num:
            criteria = has_num
        if special:
            criteria = criteria and has_special

    return pwd

min_length = int(input("Enter your desire length of password to generate : "))
pwd = gen_password(min_length)  
print("The Generated Password is : ", pwd)

