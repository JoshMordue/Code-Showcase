import pickle


def title():
    text_border("*")
    text_border("This application aims to make exercising more interesting, through the use of randomisation")
    text_border("You can tailor the amount to your liking/ability")
    text_border()
    text_border("Please press 'Enter' to start")
    text_border("*")


def text_border(text: str = " ", screen_width: int = 120) -> None:
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


def read_data(preference) -> dict:
    try with open(preference, 'r', encoding='utf-8') as user_data:
        preference =  read_data(preference)
        print(preference)
        return preference

    except FileNotFoundError:
        print(text_border('This looks to be your first time using this application'))
        print(text_border('A file will be generated during this process which will contain your preferences'))
        initial_preference(preference)


def initial_preference():
    while True:
        print(text_border('Before we begin can you please provide an exercise you perform'))
        exercise = text_border(input())


def save_data(dictionary):
    with open('Preferences.pkl', 'wb') as Saved:
        pickle.dump(dictionary, Saved)
    Saved.close()







def print_menu():
    """print menu controls"""
    print("-" * 30)
    print("MENU")
    print("-" * 30)
    print("Please enter 'A' to add a note")
    print("Please enter 'V' to view all notes")
    print("Please enter 'E' to edit a note")
    print("Please enter 'D' to delete a specified note")

