
def read_data(x, exercise):
    with open(x, 'r') as saved:
        for line in saved:
            key = line.strip()
        value = saved.readline().strip()
        exercise[key] = value

    saved.close()
    return exercise


# def save_data(x):
#     with open('Preferences.txt', 'w') as Saved:



#Squats: [1,3,4,5,6]


