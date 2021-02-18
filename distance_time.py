def main():
    time = float(input('enter time in seconds'))
    distance_1 = falling_distance(time)
    print(distance_1)
    for i in range(1, 11):
        time = i
        distance = falling_distance(i)
        print('the distance is ', format(distance, ',.2f'), sep='')
def falling_distance(t):
    d = 0.5 * 9.8 * t
    return d
main()    
