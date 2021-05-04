'''
1. Understand the problem
2. Think
3. Algorithm
4. Main Logic and start working
5. Modify

You<=>Pc<=>Internet

1. Dice
2. random face no.
3. Looping

Algorithm
1. develop random no.
2. check the no.
3. print the face
4. looping

'''
import random
print("This is a dice stimulator")
x = "y"

while x == "y":
    number = random.randint(1,6)

    if number == 1:
        print("----------")
        print("|        |")
        print("|    O   |")
        print("|        |")
        print("----------")
    if number == 2:
        print("----------")
        print("|        |")
        print("| O    O |")
        print("|        |")
        print("----------")
    if number == 3:
        print("----------")
        print("|    O   |")
        print("|    O   |")
        print("|    O   |")
        print("----------")
    if number == 4:
        print("----------")
        print("| O    O |")
        print("|        |")
        print("| O    O |")
        print("----------")
    if number == 5:
        print("----------")
        print("| O    O |")
        print("|    O   |")
        print("| O    O |")
        print("----------")
    if number == 6:
        print("----------")
        print("| O    O |")
        print("| O    O |")
        print("| O    O |")
        print("----------")
    x = input("Press << y >> to roll again = ")