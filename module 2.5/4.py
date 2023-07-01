
number = int(input("Enter the number : "))

while number:

    number = int(input("Enter the number : "))
    if number < 0:
        print("Negative")
    if number > 0:
        print("Positive")
    if number == 0:
        print("Zero")
