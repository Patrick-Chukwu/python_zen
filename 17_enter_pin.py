# A loop is used to repeat a line of code until a condition is met.
# Example: 'the while loop'


pin = int((input("Enter your ATM PIN: ")))

while pin != 1234:
    pin = int(input("PIN Incorrect. Enter Pin again!"))

print("PIN correct.")