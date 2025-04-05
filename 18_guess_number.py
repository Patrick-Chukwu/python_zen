# Let's make it so that it's the same guessing game, but there is a new limit to the number of tries (it was infinite before).

# First, introduce a variable called tries at the top and give it a value of 0.

# Then, add the tries variable to the while loop using a relational operator (like you did with guess).

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