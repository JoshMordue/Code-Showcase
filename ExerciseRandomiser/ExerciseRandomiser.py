from Functions import *

filename = 'Preferences.pkl'
# exercise_data = {'a': [0, 1, 2, 3, 4],
#                  'b': [0, 1, 2, 3, 4],
#                  'c': [0, 1, 2, 3, 4],
#                  'd': [0, 1, 2, 3, 4],
#                  }


title()

choice = input()

exercise_data = read_data(filename)

if exercise_data == {}:
    initial_preference(filename)

print(exercise_data)







