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






current_rolls(exercise_data)

print(exercise_data)
