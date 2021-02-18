import random
odd = 0
even = 0
def main():
    global odd
    global even
    for i in range(100):
        number = random.randint(1, 100)
        print(number)
        if (number % 2) == 0:
            even += 1
        else:
            odd += 1
    print(f'the number of even number is {even}')        
    print(f'the number of odd numbers is {100 - even}')
main()