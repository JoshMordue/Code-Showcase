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


def view_notes(x: list):
    """function prints all the notes found in the notes.txt file"""
    for num, note in enumerate(x):
        print("{0}: {1}".format(num + 1, note))


def edit_notes(x: list) -> list:
    """function asks for the index position and replaces the entry with the new entered note"""
    view_notes(x)
    edit_choice = int(input("Please specify the number: "))
    if edit_choice <= len(x):

        print("You're currently editing entry {0}".format(edit_choice))
        new_value = input("Please enter the edited note: ")
        x[edit_choice - 1] = new_value
    return x


def save_changes(x: list):
    """saves the supplied (altered) list to be the new values in the notepad.txt file"""
    try:
        saved_notes = '\n'.join(x)
        print(saved_notes)
        with open('Notes.txt', 'w', encoding='utf-8') as notes_file:
            notes_file.write(saved_notes)
        print("The changes have been saved.")
    except OSError:
        print("We encountered a problem saving to the directory, please assess your folder write permissions.")


def add_note(x: list) -> list:
    """requests input from the user for their new note, append the note to the new notes"""
    print("Please input your note below")
    print("-" * 30)
    new_note = input()
    x.append(new_note)
    return x


def menu():
    print("Please enter 'A' to add a note")
    print("Please enter 'v' to view all notes")
    print("Please enter 'E' to edit a note")
    print("Please enter 'D' to delete a specified note")


notes = []

print("NotePad!")
print("*" * 10)
menu()


while True:

    read_notes(notes)

    choice = input("Please enter your choice: ").upper()

    if choice == "A":
        add_note(notes)
        save_changes(notes)

    if choice == "V":
        view_notes(notes)

    if choice == "E":
        edit_notes(notes)
        save_changes(notes)

    if choice == "E":
        edit_notes(notes)
        save_changes(notes)


