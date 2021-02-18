import random
def main():
    for i in range(1, 5 + 1):
        num1 = random.randint(1, 100)
        num2 = random.randint(2, 100)
        print(f'question {i}')
        print(f'{num1} + {num2} = _______')
main()         