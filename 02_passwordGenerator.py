import string
import random

length = input('Enter the length of password (max 50) :  ')

if length.isalpha() or int(length) > 50:
    print("Only numbers are accept and the limit is 50 characters")
else:
    alphabets = string.ascii_letters
    num = string.digits
    all = alphabets + num
    temp = random.sample(all, int(length))

    password = "".join(temp)
    print(password)