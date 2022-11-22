import pickle


def read_data(exercise):
    with open('Preferences.pkl', 'rb') as opened:
        loaded_dict = pickle.load(opened)

    opened.close()
    return exercise


def save_data(dictionary):
    with open('Preferences.pkl', 'wb') as Saved:
        pickle.dump(dictionary, Saved)
    Saved.close()



