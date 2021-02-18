'''
1. Kilometer Converter
Write a program that asks the user to enter a distance in kilometers, then converts that
distance to miles. The conversion formula is as follows:
Miles 5 Kilometers 3 0.6214
'''
def main():
    #get distance in kilometers
    distance_in_km = int(input('enter distance traveled in km: '))
    # calculate the equivalentin miles
    miles =  distance_in_miles(distance_in_km)
    print('the distance is miles', format(miles, ',.2f'), sep='')

def distance_in_miles(x):
    multy = x * 0.6214
    return multy
main()    
