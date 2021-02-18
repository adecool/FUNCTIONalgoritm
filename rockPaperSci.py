import random

def main():
    user_input = int(input('enter rock for 1; enter 2 for paper and 3 for scissors: '))
    number = random.randint(1,3)
    print(number)
    while number != user_input and user_input < 4:
        if user_input == 3 and number == 1:
            print('oops!!! Rock smashes scissors')
        elif user_input == 2 and number == 1:
            print('you win') # paper raps rock
        elif user_input == 1 and number == 2:
            print('you lose')
        elif user_input == 2 and number == 3:
            print('you lose')
        elif user_input == 3 and number == 2:
            print('you win')
        elif user_input == 1 and number == 3:
            print('you win')
        break                 
main()