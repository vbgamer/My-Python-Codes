#WAP to validate age using if...else statement.

def valid():
  print("You are of age to be married")

def invalid():
  print("You are minor to be married")

age=int(input("Enter your age: "))

if (age>=21):
  valid()
else:
  invalid()

