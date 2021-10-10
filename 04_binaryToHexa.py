binary = input("Enter your binary number = ")


#BinaryArray
a = 0
b = 1
c = 2
d = 3


def hexa_binary(zaza):
    if zaza == 1:
        print('A')
    elif zaza == 2:
        print('B')
    elif zaza == 3:
        print('C')
    elif zaza == 4:
        print('D')
    elif zaza == 5:
        print('E')
    elif zaza == 6:
        print('F')
    else:
        print('Error')
    return zaza


for i in range(5):
    result = (int(binary[a]) * (2 ** 3)) + (int(binary[b]) * (2 ** 2)) + (int(binary[c]) * (2 ** 1)) + (int(binary[d]) * (2 ** 0))
    a += 4
    b += 4
    c += 4
    d += 4
    if len(str(result)) == 2:
        # list(result.strip())
        # print(str(result[0]) + str(result[1]))
        int_result = (tuple(int(x) for x in str(result)))
        hexa = int_result[0] + int_result[1]
        print(hexa_binary(hexa))
    else:
        print(hexa_binary(result))