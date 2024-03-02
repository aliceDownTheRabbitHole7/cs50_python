values = input('Calculation: ')

x, y, z = values.split(' ')

x_int = int(x)
z_int = int(z)

if y == '+':
    plus = x_int+z_int
    print(f'{plus:.1f}')
elif y == '-':
    minus = x_int-z_int
    print(f'{minus:.1f}')
elif y == '*':
    multiply = x_int*z_int
    print(f'{multiply:.1f}')
elif y == '/':
    divide = x_int/z_int
    print(f'{divide:.1f}')
else:
    print('Choose a correct operator')