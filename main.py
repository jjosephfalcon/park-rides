"""
PS11 Supplemental Project 2: Juni World

Welcome to Juni World! In this project, you are given a dictionary with the names of the various rides at Juni World and the amount of time it takes to wait and ride each ride. Park-goers have 6 hours to spend at Juni World on any rides they would like, and they have to start leaving the park once they have 15 minutes remaining or less. Write a program that continuously tells the user how much time they have remaining in Juni World, lets them choose a ride to go on, and prints out all of the rides they went on in order at the end of the day.
"""
# Dictionary Keys: The ride names 
# Dictionary Values: Number of minutes per ride wait
 
ridesDict = {
  'Tower of Turtles': 90,
  'String Mountain': 130,
  'Debug Track': 5,
  'Concatenation cucumber': 100,
  'Cinderella Casting': 90,
  'Magic For Loop': 10,
  'Pythons of the Carribean': 30
}
# 6 hours * 60 mins = 360 mins 
time_remaining = 360

while True: 
  print("Time remaining: ", time_remaining)

  print("""
  1) Tower of Turtles
  2) String Mountain
  3) Debug Track
  4) Concatenation cucumber
  5) Cinderella Casting
  6) Magic For Loop
  7) Pythons of the Carribean
  """)

  choice = input("Pick a ride (1-7): ")
  
  if choice == '1':
    time_remaining -= ridesDict['Tower of Turtles']
  
  elif choice == '2':
    time_remaining -= ridesDict['String Mountain']

  elif choice == '3':
    time_remaining -= ridesDict['Debug Track']

  elif choice == '4':
    time_remaining -= ridesDict['Concatenation cucumber']
  
  elif choice == '5':
    time_remaining -= ridesDict['Cinderella Casting']
  
  elif choice == '6':
    time_remaining -= ridesDict['Magic For Loop']
  
  elif choice == '7':
    time_remaining -= ridesDict['Pythons of the Carribean']

  
  # If time_remaining is less than 15...must leave park!
  if time_remaining < 15:
    print("Your time is up, must leave park!")
    break

  
  

  # For each of the choices use a differnt key (name of ride) to get the value we have to subtract from time_remaining. 

  # in the above example we subtracted 'Tower of Turtles', when the user choice was number 1.

    


  # Once you complete the 7 choices, at the bottom check if the time remaining is 15 or less. 
  # If it is 15 or less, then the park visit is over. (print that)
  




# HomeWork:
# Lists! 
# How do you get something from a list? 

# letters = ['a', 'b', 'c', 'd', 'e']

# # print 'c' from letters
# # print(letters[2])

# # add 'f' to the letters list

# letters.append('f')
# # print(letters)
# # remove 'd' from the letters list 

# letters.remove('d')
# # print(letters)
# # Loop through letters and print each letter
# # capitalize each letter using .upper() 
# # for i in letters:
# #   print(i.upper())

# # Dictionary
# bank = {'balance': 1000}
# print("Bank: ", bank)
# # Buy a computer: $812

# bank['balance'] -= 812 
# print("Bank After computer: ", bank)

# # You're walking your cat...and you find $400!!!! 
# bank['balance'] += 400 

# print("Bank after getting rich: ", bank)











