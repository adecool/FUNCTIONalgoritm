Assessment_value = 0.6
property_tax = 0.0072

def main():
    property_value = int(input('enter the value of property in dollars: '))
    assess = get_assessment(property_value)
    tax = get_property_tax(assess)
    print(f'the equivalen assesment value and property tax are as follow: ${assess}, $', format(tax, ',.2f'), sep='')
def get_assessment(x):
    y = x * Assessment_value
    return y
def get_property_tax(p):
    t = p * property_tax
    return t   
main()
def main2():
    fat_grams = int(input('enter the amount of fat in grams in diet: '))
    carb_grams = int(input('enter the amount of carbohydrates in geams in diet: '))
    carbohydrates = calories_carb(carb_grams)
    fat = calories_fat(fat_grams)
    print('the number of calories from fat is', fat)
    print('the number of calories in carbohydrates is', carbohydrates)    
def calories_fat(f):
    y = f * 9
    return y
def calories_carb(c):
    m = c * 4
    return m
main2()        

