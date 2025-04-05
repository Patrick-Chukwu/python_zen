guess = 0
tries = 0

while guess != 6 and tries < 3:
  guess = int(input("Guess the number:  "))
  tries = tries + 1

if tries > 3:
  print("You run out of time.")
elif guess != 6:
  print("Not correct!")
else:
   print("You got it!")