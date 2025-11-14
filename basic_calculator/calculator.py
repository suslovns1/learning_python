import math

# Об'являю Dictionary з назвою operations, котра буде містити в собі дані про кожну з операцій, котрі потім будуть використовуватися у виконанні безпосередньо. 
def calculator_addition(first_int, second_int):
    result = first_int + second_int
    return result

def calculator_substraction(first_int, second_int):
    result = first_int - second_int
    return result
    
def calculator_miltiplication(first_int, second_int):
    result = first_int * second_int
    return result

def calculator_division(first_int, second_int):
    result = first_int / second_int
    return result

def calculator_exponent(first_int, second_int):
    result = pow(first_int, second_int)
    return result

def calculator_squareRoot(first_int):
    result = math.sqrt(first_int)
    return result

def calculator_triangleHypotenuse(first_int, second_int):
    result = math.sqrt(math.pow(first_int, 2) + math.pow (second_int, 2))
    return result


operations = {
      "1" : ("addition", calculator_addition, 2),
      "2" : ("substraction", calculator_substraction, 2), 
      "3" : ("miltiplication", calculator_miltiplication, 2 ),
      "4" : ("division", calculator_division, 2),
      "5" : ("exponent", calculator_exponent, 2),
      "6" : ("squareRoot", calculator_squareRoot, 1),
      "7" : ("triangleHypotenuse", calculator_triangleHypotenuse, 2),
      "0" : ("exit", 0, 0)
}

# First stage - Choose your operation.
print("""
      1 — Addition
      2 — Subtraction
      3 — Multiplication
      4 — Division
      5 — Exponent (a^b)
      6 — Square root
      7 — Triangle hypotenuse
      0 — Exit""")
userInput = input("Please enter operation number: ")

# Second stage - checking whether entered data is integer.
if userInput == "0":
    print(operations["0"][3])
    exit()

if userInput not in operations:
    print("Error: Invalid operation number!")
    exit()
    
# Third stage - entering numbers and performing calculations. 
if operations[userInput][2] == 2:
    input_number_a = float(input("Enter your first number: "))
    input_number_b = float(input("Enter your second number: "))
    round(print(f"Result of your operations is: {operations[userInput][1](input_number_a, input_number_b)}"), 1)
elif operations[userInput][2] == 1:
    input_number = float(input("Enter your number: "))
    round(print(f"Result of your operations is: {operations[userInput][1](input_number)}"), 1)
else:
    print("See you later!") 
    
exit() 
    