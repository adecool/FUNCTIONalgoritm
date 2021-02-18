def main():
    number_in_ft = get_num_feet()
    number_in_inches = calc_no_in_inches(number_in_ft)
    print(f'{number_in_ft}ft is equivalent to {number_in_inches}inches')
def get_num_feet():
    feet = int(input('enter the number in feet: '))
    return feet
def calc_no_in_inches(x):
    inches = x * 12
    return inches
main()