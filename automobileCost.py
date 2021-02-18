'''4. Automobile Costs
Write a program that asks the user to enter the monthly costs for the following expenses
incurred from operating his or her automobile: loan payment, insurance, gas, oil, tires, and
maintenance. The program should then display the total monthly cost of these expenses,
and the total annual cost of these expenses.
'''
def main():
    loan_payment = get_loan_pay()
    insurance_cost = get_insurance()
    gas = gas_cost()
    tires = tires_cost()
    oil = oil_cost()
    maintenance = maintenance_cost()
    total_cost = show_total(loan_payment,insurance_cost,gas,tires,oil,maintenance)
    annual_cost = get_annual_cost(total_cost)
    print(f'the total cost for this month is ${total_cost}')
    print(f'the total cost for this year expenditures is ${annual_cost}')
def get_loan_pay():
    loan = int(input('what is the monthly loan pay'))
    return loan
def get_insurance():
    insur = int(input('enter monthly insurance cost: '))
    return insur
def gas_cost():
    gas = int(input('enter monthly cost: '))
    return gas
def tires_cost():
    tire = int(input('enter the costof the tire: '))
    return tire    
def oil_cost():
    oil = int(input('enter monthly cost: '))
    return oil
def maintenance_cost():
    maintenance = int(input('enter monthly cost: '))
    return maintenance
def show_total(u,v,w,x,y,z):
    sum = u + v + w + x + y + z 
    return sum
def get_annual_cost(x):
    annual = x * 12
    return annual        
main()    