def main():
    num1 = int(input('enter a number'))
    num2 = int(input('enter a number'))
    max_num = max_print(num1,num2)
    print(max_num)
def max_print(x,y):
    if x > y:
        return f'{x} is greater than {y}'
    elif x < y:
        return f'{y} is greater than {x}'
    else:
        return 'both numbers are equal'
main()                    