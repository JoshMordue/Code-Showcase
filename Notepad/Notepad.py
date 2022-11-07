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
        print(x)
        print("{0}: {1}".format(num + 1, note))


def menu():
    print("NotePad!")
    print("*" * 10)
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