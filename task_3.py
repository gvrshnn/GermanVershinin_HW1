first_number = float(input())
second_number = float(input())
operation = str(input())
if operation in ('+-/*modpowdiv'):
    if operation == '+':
        print(first_number + second_number)
    elif operation == '-':
        print(first_number - second_number)
    elif operation == '*':
        print(first_number * second_number)
    elif operation == '/':
        if second_number == 0:
            print('Division by 0!')
        else:
            print(first_number / second_number)
    elif operation == 'mod':
        if second_number == 0:
            print('Division by 0!')
        else:
            print(first_number % second_number)
    elif operation == 'pow':
        print(first_number ** second_number)
    elif operation == 'div':
        if second_number == 0:
            print('Division by 0!')
        else:
            print(first_number // second_number)
else:
    print('Supported operations: +, -, /, *, mod, pow, div')
