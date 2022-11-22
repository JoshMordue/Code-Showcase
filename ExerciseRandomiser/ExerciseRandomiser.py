import json
from Functions import *

filename = 'Preferences.txt'
exercise_data = {}


word_list = read_data(filename, exercise_data)

for k, v in exercise_data.items():
    print(k)
    v, sep='\n'



