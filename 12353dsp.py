import math

while True:
    # Display a menu
    print('Scientific Calculator')
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    print('5. Exponentiation')
    print('6. Square Root')
    print('7. Sine')
    print('8. Cosine')
    print('9. Tangent')
    print('10. Logarithm (base 10)')
    print('11. Natural Logarithm (base e)')
    print('12. Quit')

    # Get user choice
    choice = int(input('Enter your choice: '))

    if choice == 12:
        # Quit the calculator
        print('Exiting the calculator.')
        break

    if choice in range(1, 12):
        # For operations 1-11
        if choice in [1, 2, 3, 4, 5]:
            a = float(input('Enter the first number: '))
            b = float(input('Enter the second number: '))
        elif choice in [6, 7, 8, 9, 10, 11]:
            a = float(input('Enter a number: '))

        if choice == 1:
            result = a + b
        elif choice == 2:
            result = a - b
        elif choice == 3:
            result = a * b
        elif choice == 4:
            if b == 0:
                print('Error: Division by zero is not allowed.')
                continue
            result = a / b
        elif choice == 5:
            result = a ** b
        elif choice == 6:
            if a < 0:
                print('Error: Square root of a negative number is not defined.')
                continue
            result = math.sqrt(a)
        elif choice == 7:
            result = math.sin(math.radians(a))
        elif choice == 8:
            result = math.cos(math.radians(a))
        elif choice == 9:
            result = math.tan(math.radians(a))
        elif choice == 10:
            if a <= 0:
                print('Error: Logarithm of a non-positive number is not defined.')
                continue
            result = math.log10(a)
        elif choice == 11:
            if a <= 0:
                print('Error: Natural logarithm of a non-positive number is not defined.')
                continue
            result = math.log(a)

        print('Result: {:.2f}'.format(result))

    else:
        print('Invalid choice. Please select a valid option.')
