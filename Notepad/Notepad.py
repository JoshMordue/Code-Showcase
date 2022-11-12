import sys


def read_notes(x):
    """Function to retrieve notes if they exist, if it does not create an empty """
    try:
        with open('Notes.txt', 'r', encoding='utf-8') as notes_file:
            for line in notes_file:
                x.append(line.strip("\n"))

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


def view_notes(x: list):
    """function prints all the notes found in the notes.txt file"""
    print("VIEWING NOTES")
    print("*" * 50)
    if not x:
        print("There are no notes present in your notepad")
    for num, note in enumerate(x):
        print("{0}: {1}".format(num + 1, note))
    return x


def edit_note(x: list):
    """function asks for the index position and replaces the entry with the new entered note"""
    print("EDITING NOTES MENU")
    print("*" * 50)
    view_notes(x)
    edit_choice = int(input("Please specify the number of the entry: "))
    if edit_choice <= len(x):
        print("You're currently editing entry {0}".format(edit_choice))
        new_value = input("Please enter the edited note: ")
        x[edit_choice - 1] = new_value
        save_changes(x)
        return x


def save_changes(x: list):
    """saves the supplied (altered) list to be the new values in the notepad.txt file"""
    try:
        saved_notes = '\n'.join(x)
        with open('Notes.txt', 'w', encoding='utf-8') as notes_file:
            notes_file.write(saved_notes)
        print("-" * 20)
        print("The changes have been saved.")
        print("-" * 20)
        return x
    except OSError:
        print("We encountered a problem saving to the directory, please assess your folder write permissions.")


def add_note(x: list):
    """requests input from the user for their new note, append the note to the new notes"""
    print("ADDING NOTES MENU!")
    print("Please input your note below")
    print("-" * 30)
    new_note = input()
    x.append(new_note)
    save_changes(x)
    return x


def del_note(x: list):
    view_notes(x)
    print("DELETING NOTES MENU!")
    print("Please input the specific note number you want deleted, if you wish to delete all notes type 0")
    print("*" * 50)
    while True:
        del_choice = int(input())

        if del_choice == 0:
            x = []
            save_changes(x)
            return x

        elif 0 < del_choice <= len(x):
            x.pop(del_choice - 1)
            save_changes(x)
            return x
        print("Please enter a valid note number to delete")


def menu():
    print("Please enter 'A' to add a note")
    print("Please enter 'V' to view all notes")
    print("Please enter 'E' to edit a note")
    print("Please enter 'D' to delete a specified note")


print("NotePad!")
print("*" * 10)

while True:
    notes = []
    read_notes(notes)

    menu()

    choice = input("Please enter your choice: ").upper()

    print("-" * 30)

    if choice == "A":
        choice = ""
        add_note(notes)

    if choice == "V":
        choice = ""
        view_notes(notes)

    if choice == "E":
        choice = ""
        edit_note(notes)

    if choice == "E":
        choice = ""
        edit_note(notes)

    if choice == "D":
        choice = ""
        del_note(notes)
