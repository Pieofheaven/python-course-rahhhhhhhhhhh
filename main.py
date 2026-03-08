from random import choice

allowed_characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password_req = int(input("введи длину пароля "))
password = ''

for i in range(password_req):
    password += choice(allowed_characters)

print (password)