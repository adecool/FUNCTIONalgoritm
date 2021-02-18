#a
def main():
    number = int(input('enter a number to check: '))
    test_Prime = is_Prime(number)
    if test_Prime == False:
        print(f'{number} is not a prime number')
    else:
        print('it is a prime number')      
def is_Prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if(num % i) == 0:
            return False
    return True              


# b
for i in range(900,1000 + 1):
    if is_Prime(i) == True:
        print(i)
    else:
        pass               