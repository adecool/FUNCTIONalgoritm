'''
The number of gallons of paint required
• The hours of labor required
• The cost of the paint
• The labor charges
• The total cost of the paint job
'''
def main():
    square_feet_required = get_square_feet()
    paint_per_gallon = get_price_paint_gallon()
    no_of_gallon = calc_no_of_gallon(square_feet_required)
    hours_of_labor = calc_hours_of_labor(square_feet_required)
    cost_of_paint = calc_cost_of_paint(no_of_gallon, paint_per_gallon)
    labour_charges = calc_labor_charges(hours_of_labor)
    total_cost = calc_total_cost(labour_charges, cost_of_paint)  
    print(f'The number of gallons of paint required {no_of_gallon}')
    print(f'The hours of labor required {hours_of_labor}hrs')
    print(f'The cost of the paint ${cost_of_paint}')
    print(f'The labor charges ${labour_charges}')
    print(f'The total cost of the paint job ${total_cost}')
def get_square_feet():
    square_ft = int(input('enter the square feet of the wall to be painted: '))
    return square_ft
def get_price_paint_gallon():
    paint_gallon = int(input('enter the price of paint per gallon'))
    return paint_gallon
def calc_no_of_gallon(x):
    gallon_num = x // 112
    return gallon_num
def calc_hours_of_labor(y):
    hours_required = (y * 8) // 112
    return hours_required
def calc_cost_of_paint(y, z):
    cost_paint = y * z
    return cost_paint
def calc_labor_charges(x):
    charges_for_labour = x * 35
    return charges_for_labour
def calc_total_cost(x,y):
    total_charges = x + y
    return total_charges    
main()

