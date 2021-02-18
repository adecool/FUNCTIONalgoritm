Total = 0
def main():
    global Total
    for i in range(1,6):
        number = int(input('enter test score: '))
        Total += number
        determine_grade(number)    
    calc_average(Total) 

def determine_grade(num):
    if num >89 and num <= 100:
        print(f'{num} is a A')
    elif num >79 and num <= 89:
        print(f'{num} is a B')
    elif num >69 and num <= 79:
        print(f'{num} is a C')
    elif num >59 and num <= 69:
        print(f'{num} is a D')
    else:
        print(f'{num} is F')
def calc_average(Total):
    average = Total / 5
    print('the average test score is: ', average)
main()               
