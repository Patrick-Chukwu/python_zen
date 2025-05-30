# Recap:
# We have just three logical operators: 'and', 'or', ' not'
# We have six relational operators: '==', '!=', '<', '>', '<=', '>='


# Instructions
# The Sorting Hat is a magical talking hat at Hogwarts School of Witchcraft and Wizardry. The hat decides which of the four "Houses" each first-year student goes to:

# 🦁 Gryffindor
# 🦅 Ravenclaw
# 🦡 Hufflepuff
# 🐍 Slytherin


# Write a program that asks the user some questions with the int() and input() functions:

# Q1) Do you like Dawn or Dusk?
#     1) Dawn
#     2) Dusk

# If answer is equal to 1, Gryffindor and Ravenclaw both get a +1.
# Else if answer is equal to 2, Hufflepuff and Slytherin both get a +1.
# Else, output the message "Wrong input."
# Q2) When I’m dead, I want people to remember me as:
#     1) The Good
#     2) The Great
#     3) The Wise
#     4) The Bold

# If the answer is 1, Hufflepuff +2.
# Else if answer is 2, Slytherin +2.
# Else if answer is 3, Ravenclaw +2.
# Else if answer is 4, Gryffindor +2.
# Else, output the message "Wrong input."
# Q3) Which kind of instrument most pleases your ear?
#     1) The violin
#     2) The trumpet
#     3) The piano
#     4) The drum

# If the answer is 1, Slytherin +4.
# Else if the answer is 2, Hufflepuff +4.
# Else if the answer is 3, Ravenclaw +4.
# Else if the answer is 4, Gryffindor +4.
# Else, output "Wrong input."
# Lastly, print out the score for each house.

# Bonus: If you want to go further, see if you can figure out how to print out the house with the most points!


# Q1
answer = int(input('Do you like Dawn or Dusk? \n 1) Dawn \n 2)Dusk \n' ))

if answer == 1:
  print("Gryffinder and Ravenclaw both get a +1.")
elif answer == 2:
  print("Hufflepuff and Slytherin both get a +1")

else:
    print("Wrong input.")

# Q3:

instrument = int(input("Which kind of instrument most pleases your ear? \n 1) The Violin \n 2) The trumpet \n 3) The piano \n 4) The drum  \n"))

if instrument == 1:
  print("Slytherin +4.")
elif instrument == 2:
  print("Hufflepuff +4.")
elif instrument == 3:
  print("Ravenclaw +4")
elif instrument == 4:
  print("Gryffinder +4")
else:
  print("Wrong input.")

