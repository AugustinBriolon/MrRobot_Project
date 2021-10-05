import string
import random

length = int(input('\nEnter the length of password: '))
alphabets = string.ascii_letters
num = string.digits

all = alphabets + num

temp = random.sample(all,length)
password = "".join(temp)

print(password)
