import random
import time
a = "abcdefghijklmnopqrstuvwxyz"
b = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
с = "0123456789"
d = "{}[]*/,!?"

all = a + b + с + d
# length = int(input("Enter expected password length"))
while True:
    try:
        length = int(input("Enter expected password length: "))
        if length <5:
            print("We recommend to choose from 5 to 12 symbols")
            time.sleep(1)
        elif length >15:
            print("It`s too long password, we recommend the length about 12 symbols")
            time.sleep(1)
        else:
            password = "".join(random.sample(all, length))
            print("Generation is going...")
            time.sleep(2)
            print("Your password is ready")
            print(password)
            break
    except ValueError:
        print("Please enter the integer")