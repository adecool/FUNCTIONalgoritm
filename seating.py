'''
7. Stadium Seating
There are three seating categories at a stadium. Class A seats cost $20, Class B seats cost
$15, and Class C seats cost $10. Write a program that asks how many tickets for each class
of seats were sold, then displays the amount of income generated from ticket sales.
'''
def main():
    a = classA()
    b = classB()
    c = classC()
    amount =amount_of_income(a,b,c)
    print('the total amount of income from the tickets sold is: ', amount)
def classA():
    e = int(input('enter numbr of a ticket'))
    valA = 20 * e
    return valA
def classB():
    d = int(input('enter numbr of b ticket'))
    valB = 15 * d
    return valB
def classC():
    f = int(input('enter numbr of c ticket'))
    valC = 10 * f
    return valC
def amount_of_income(a,b,c):
    z = a + b + c
    return z
main()