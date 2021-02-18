import random
def main():
    guess_Number = int(input('enter your guess:'))
    random_num = get_number()
    guess_count = 0
    guess_limit = 3
    while guess_Number != random_num and guess_count < guess_limit:
        guess_count+=1
        if random_num < guess_Number:
                print('number is to high')
                print(f'you have {guess_limit - guess_count} more tries')
        elif random_num > guess_Number:
            print('number is to low')
            print(f'you have {guess_limit - guess_count} more tries')
        guess_Number = int(input('enter your guess:'))    
    if random_num == guess_Number:
        print('correct')
    else:
        print('oops!!!, game over try again')
        print(random_num)    
def get_number():
    number = random.randint(1, 50)
    return number
main()                       
