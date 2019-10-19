import random

while True:
    num = int(input("Pick a number: "))
    comp_numb = random.randint(1,4)
    def number_guess():
        if comp_numb == 1:
            print("The number is 1")
        elif comp_numb == 2:
            print("The number is 2")
        elif comp_numb == 3:
            print("The number is 3")
        elif comp_numb == 4:
            print("The number is 4")
    if num == comp_numb:
        print("Congratulations! You guessed correctly!")
    else:
        print("You guessed incorrectly! Would you like to try again?")
    if input("Y/N? ") == "N":
        break





