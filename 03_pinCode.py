import hashlib

hash = "8a069869956a4e0cf7ac69f9c20e0d49"

i = 72000000
while i <= 99999999:
    print(i)
    iHash = hashlib.md5(str(i).encode())
    print(iHash.hexdigest())
    if iHash.hexdigest() == hash:
        print(f"We find the password, it's : {i}" )
        break
    elif i == 99999999:
        print('Password not find')
    i += 1