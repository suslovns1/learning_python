# Step 1. Verify user input for correct data type and quantity.
# Initial Principal Define
while True:
    try:
        initial_principal = float(input("Please enter your Initial Principal: "))
        if initial_principal <= 0:
            print("Please, enter a number higher than 0.")
            initial_principal = float(input("Please enter your Initial Principal: "))
        else:
            break
    except ValueError:
        print("Error! Please, enter a number.")

# Interest Rate Define
while True:
    try:
        interest_rate = float(input("Please enter your Interest Rate: ")) / 100
        if interest_rate <= 0:
            print("Please, enter a number higher than 0.")
            interest_rate = float(input("Please enter your Interest Rate: ")) / 100
        else:
            break
    except ValueError:
        print("Error! Please, enter a number.")

# Loan Term Define
while True:
    try:
        term = int(input("Please enter your Loan Term: "))
        if term <= 0:
            print("Please, enter a number higher than 0.")
            term = int(input("Please enter your Loan Term: "))
        else:
            break
    except ValueError:
        print("Error! Please, enter a integer.")

# Compounding Frequency Define
while True:
    try:
        compound_frequency = int(input("""Please enter your Compound Frequency (times during year):
                                       1 - Yearly
                                       4 - Quarterly
                                       12 - Monthly
                                       365 - Daily
                                       Your Compound Frequency: """))
        if compound_frequency <= 0 or compound_frequency > 365:
            print("Please, enter a number higher than 0 and lower than 365")
            compound_frequency = int(input("""Please enter your Compound Frequency (times during year):
                                       1 - Yearly
                                       4 - Quarterly
                                       12 - Monthly
                                       365 - Daily
                                       Your Compound Frequency: """))
        else:
            break
    except ValueError:
        print("Error! Please, enter a integer.")

# Step 2. Calculation of the final amount after interest has been paid.
x = 0

result_principal = initial_principal

while x < term*compound_frequency:
    result_principal = result_principal * (1 + (interest_rate / compound_frequency))
    x += 1

# Step 3. Output of final loan information to the console.

print(f"Total amount payable, after interest has been calculated for {term} years: \n{round(result_principal,2):=^20}")
print(f"Total interest accrued on the loan: \n{round(result_principal - initial_principal, 2):=^20}")




