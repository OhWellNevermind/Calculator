x = float(input('x: '))
z = float(input('y: '))

operation = input('Operation: ')

result = None

if operation == '+':
    result = x + z
elif operation == '-':
    result = x - z
elif operation == '*':
    result = x * z
elif operation == '/':
    result = x / z



if result is not None:

 print(result)