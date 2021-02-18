def main():
    mass = int(input('enter the mass in kilogram: '))
    velocity = float(input('enter the velocity of tht body: '))
    kinetic_e = kinetic_energy(mass,velocity)
    print(f'the kinetic Energy is {kinetic_e}J')
def kinetic_energy(x,y):
    KE = 0.5 * x * (y)**2
    return KE
main()        