# Take a number as input and check if its a prime

while True:
    try:
        num = int(input("Enter a number: "))
        if num < 0:
            print("Please enter a value greater than 0")
            continue
        break
    except ValueError:
        print("Please enter a valid number")


if num > 1:
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")