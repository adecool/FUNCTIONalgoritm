def main():
    num = int(input('enter the total sales for the month: '))
    states_tax = calc_states_tax(num)
    country_tax = calc_county_tax(num)
    total_tax = total_monthly_tax(states_tax, country_tax)
    print(f'the following are the states tax,'
    + f'country tax and the total tax for the months resp.' 
    + f'${states_tax}, ${country_tax}, ${total_tax}')
def calc_states_tax(x):
    states = x * 0.05
    return states
def calc_county_tax(x):
    country = x * 0.025
    return country
def total_monthly_tax(x,y):
    sum_tax = x + y
    return sum_tax    
main()
