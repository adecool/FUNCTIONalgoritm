'''
The terms in the formula are:
• P is the payment amount per month.
• R is the monthly interest rate, as a decimal (e.g. 2.5% 5 0.025).
• A is the amount of the loan.
• M is the number of months.
'''
def main():
    A = int(input('the amount of the loan: '))
    R = float(input('the monthly interest rate, as a decimal (e.g. 2.5% 5 0.025).'))
    M = int(input('the number of months: '))
    payment_per_month = calc_Amount(R,A,M)
    print('the monthly payment amount neccessary is $', format(payment_per_month, ',.2f'), sep='')
def calc_Amount(x,y,z):
    pay = (x * y) / (1-(1 + x)**(-z))
    return pay
main()    
