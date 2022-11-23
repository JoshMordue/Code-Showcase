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


def title():
    print("*" * 30)
    print("This application aims to make exercising more interesting, through the use of randomisation")
    print("You can tailor the amount to your liking/ability - the system will use defaults until it's been configured")
    print()
    choice = input("Please press 'Enter' to start")
    print("*" * 30)



def print_menu():
    """print menu controls"""
    print("-" * 30)
    print("MENU")
    print("-" * 30)
    print("Please enter 'A' to add a note")
    print("Please enter 'V' to view all notes")
    print("Please enter 'E' to edit a note")
    print("Please enter 'D' to delete a specified note")

