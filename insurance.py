'''
3. How Much Insurance?
Many financial experts advise that property owners should insure their homes or buildings
for at least 80 percent of the amount it would cost to replace the structure. Write a program
that asks the user to enter the replacement cost of a building, then displays the minimum
amount of insurance he or she should buy for the property.
'''
def main():
    replacement_cost = int(input('enter the replacementcost of the structure:'))
    min_insusrance_cost(replacement_cost)
def min_insusrance_cost(x):
    num = x * 0.8
    print(num)
main()    
