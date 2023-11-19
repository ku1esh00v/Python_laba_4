a = float(input('Enter a smaller base: '))
b = float(input('Enter a larger base: '))
h = float(input('Enter the height drawn on a larger base: '))

bokovoe_rebro = (h**2 + ((b - a) / 2)**2)**(1 / 2)

P = a + b + (2 * bokovoe_rebro)

print('The perimeter is equal to', P)
