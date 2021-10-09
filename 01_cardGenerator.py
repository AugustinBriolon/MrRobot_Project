import random
import sys

type = input("Vista or Mastercard only >").lower()

def card_generator(number=0):

    card = list("0000000000000000")

    for i in range(16):

        number = random.randrange(0, 9)

        card[i] = card[i].replace("0", str(number))

    if type == "visa":
        card[0] = '4'
        new_card = "".join(card)
    elif type == "mastercard":
        card[0] = '5'
        new_card = "".join(card)
    else:
        print("Error with your type of card (use only visa or mastercard)")
        sys.exit()

    new_card = new_card[::-1]
    sum = 0
    for i in range(1, 16, 2):
        mult = int(new_card[i]) *2
        if mult > 9:
            mult -= 9
        sum += mult
    for i in range(0, 16, 2):
        mult2 = int(new_card[i])
        sum += mult2
    if sum%10 == 0:
        return new_card[::-1]
    else:
        return card_generator()

print(f"Your card number is : {card_generator()}")