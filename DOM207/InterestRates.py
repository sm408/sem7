#taking principal balance in INR from user
while True:
    try:
        principal = float(input("Enter principal balance in INR: "))
        if principal < 0:
            print("Please enter a value greater than 0")
            continue
        break
    except ValueError:
        print("Please enter a valid number")

#taking interest rate from user
while True:
    try:
        interest_rate = float(input("Enter interest rate: "))
        if interest_rate < 0:
            print("Please enter a value greater than 0")
            continue
        break
    except ValueError:
        print("Please enter a valid number")

#taking number of times interest applied per time period from user
while True:
    try:
        times_applied = int(input("Enter the number of times interest applied per time period: "))
        if times_applied < 0:
            print("Please enter a value greater than 0")
            continue
        break
    except ValueError:
        print("Please enter a valid number")

#taking time period for investment in years from user
while True:
    try:
        time_period = float(input("Enter time period for investment in years: "))
        if time_period < 0:
            print("Please enter a value greater than 0")
            continue
        break
    except ValueError:
        print("Please enter a valid number")

compound_interest = principal * ((1 + (interest_rate / (100*times_applied)) ** (times_applied * time_period)))

print("Total compound interest: ", compound_interest)