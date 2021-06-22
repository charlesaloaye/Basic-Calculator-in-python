# Python Calculator
print("Basic Calculator in Python")

# Addition Function
def add_numbers(first_value, second_value):
    
    answer =  first_value + second_value

    return answer

    # Substraction Function
def minus_numbers(first_value, second_value):
    
    answer =  first_value - second_value

    return answer

    # Multiplication Function
def times_numbers(first_value, second_value):
    
    answer =  first_value * second_value

    return answer

    # Division Function
def divide_numbers(first_value, second_value):
    
    answer =  first_value + second_value

    return answer

# Commands
command = int(input("Enter Command \n 1. For Addition \n 2. For Subtraction\n 3. For Multiplication\n 4. For Division \n"))

num1 = int(input('Enter first number\n'))
num2 = int(input('Enter second number\n'))


if command == 1:
    print(num1, "+", num2, "=", add_numbers(num1, num2))

elif command == 2:
    print(num1, "-", num2, "=", minus_numbers(num1, num2))

elif command == 3:
    print(num1, "*", num2, "=", times_numbers(num1, num2))

elif command == 4:
    print(num1, "/", num2, "=", divide_numbers(num1, num2))

else:
    print('Invalid command')
