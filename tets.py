
# Existing code
print('coool')
print("Ok, I'm done now.")
print("I'm really done now.")

# New functionality to enter two digits and multiply them
def multiply_two_digits():
    try:
        num1 = int(input("Enter the first digit: "))
        num2 = int(input("Enter the second digit: "))
        result = num1 * num2
        print(f"The result of multiplying {num1} and {num2} is {result}.")
    except ValueError:
        print("Invalid input. Please enter valid digits.")

# Call the function
multiply_two_digits()

print("A brand new branch.")
a = 5