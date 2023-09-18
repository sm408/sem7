USDtoINR = 83.2

# ask user for USD value between $1000 to $6000, values inclusive
# dollar value input has a try except for a ValueError and loop until correct value is entered

while True:
    try:
        USD = float(input("Enter USD value between $1000 to $6000: "))
        if USD < 1000 or USD > 6000:
            print("Please enter a value between $1000 to $6000")
            continue
        break
    except ValueError:
        print("Please enter a valid number")

# convert USD to INR
print("USD to INR: ", USD * USDtoINR)
