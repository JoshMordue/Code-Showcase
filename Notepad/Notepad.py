import sys


def read_notes(x):
    """Function to retrieve notes if they exist, if it does not create an empty """
    try:
        with open('Notes.txt', 'r', encoding='utf-8') as notes_file:
            for line in notes_file:
                x.append(line.strip("\n"))
        return x

    except FileNotFoundError:
        print()
        print("As this is your first time loading this application, a new 'Note.txt' file will be generated")
        print()
        agreement = input("For this to work we would need your consent, type 'Y' to Agree otherwise type 'N': ").lower()
        if agreement == 'y':
            open('Notes.txt', 'w').close()
            print()
            print("File has been successfully generated")
            print()
            read_notes(notes)
        else:
            print()
            print('This is a required process for the application to run, please reload the application to try again')
            sys.exit()


def view_notes(x):
    for num, note in enumerate(x):
        print("{0}: {1}".format(num + 1, note))


def edit_notes(x):
    view_notes(x)
    edit_choice = int(input("Please specify the number: "))
    if edit_choice <= len(x):
        print("You're currently editing entry {0}".format(edit_choice))
        new_value = input("Please enter the edited note: ")
        x[edit_choice - 1] = new_value
        save_changes(x)

    return x


def save_changes(x):
    try:
        with open('Notes.txt', 'w', encoding='utf-8') as notes_file:
            notes_file.writelines(x)




        print("The changes have been saved.")
    except OSError:
        print("We encountered a problem saving to the directory, please assess your folder write permissions.")


def menu():
    print("NotePad!")
    print("*" * 10)
    print("Please enter 'A' to add a note")
    print("Please enter 'v' to view all notes")
    print("Please enter 'E' to edit a note")
    print("Please enter 'D' to delete a specified note")


notes = []
read_notes(notes)
menu()

while True:
    print(notes)

    choice = input("Please enter your choice: ")

    if choice == "V":
        view_notes(notes)

    if choice == "E":
        edit_notes(notes)