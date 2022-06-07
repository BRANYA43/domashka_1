x = ''
y = ''

while not x.isdigit() and not y.isdigit():
    x = input('Введите число для x: ')
    y = input('Введите число для y: ')

x = int(x)
y = int(y)

print(f'x = {x}, y = {y}')
print(f'{x} + {y} = {x + y}')
print(f'{x} // {y} = {x // y}')
print(f'{x} % {y} = {x % y}')
print(f'{x}^{y} = {x ** y}')

