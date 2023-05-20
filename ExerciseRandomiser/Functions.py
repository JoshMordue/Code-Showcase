import pickle


def title():
    menu_text("*")
    menu_text("This application aims to make exercising more interesting, through the use of randomisation")
    menu_text("You can tailor the amount to your liking/ability - "
              "the system will use defaults until it's been configured")
    menu_text()
    menu_text("Please press 'Enter' to start")
    menu_text("*")


def menu_text(text: str = " ", screen_width: int = 120) -> None:
    """
    This function prints a string centred with ** on either side.

    :param text: the string which is printed
        An asterisk will print a line full of asterisks and if the
        default value is passed through " " it'll just print ** on each side.
    :param screen_width: the canvas size to print the left and right "**" on.
    :raises ValueError: If supplied with a string which is too long to fit.
    """
    if len(text) > screen_width - 4:
        raise ValueError("String {0} is larger than specified width {1}"
                         .format(text, screen_width))

    if text == "*":
        print("*" * screen_width)
    else:
        output_string = "**{0}**".format(text.center(screen_width - 4))
        print(output_string)


def read_data(preference):
    try:
        with open(preference, 'r', encoding='utf-8') as user_data:
            preference = pickle.load(user_data)






def read_data(exercise):
    with open('Preferences.pkl', 'rb') as opened:
        exercise = pickle.load(opened)

    opened.close()
    return exercise


def save_data(dictionary):
    with open('Preferences.pkl', 'wb') as Saved:
        pickle.dump(dictionary, Saved)
    Saved.close()



def current_rolls(exercise):
    for k in exercise:
        v = exercise[k]
        menu_text(k)
        menu_text(v)




def print_menu():
    """print menu controls"""
    print("-" * 30)
    print("MENU")
    print("-" * 30)
    print("Please enter 'A' to add a note")
    print("Please enter 'V' to view all notes")
    print("Please enter 'E' to edit a note")
    print("Please enter 'D' to delete a specified note")

