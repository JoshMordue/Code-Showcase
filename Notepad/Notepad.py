def read_notes(x):
    """Function to retrieve notes if they exist"""
    try:
        x = open('Notes.txt', 'rb')
    except FileNotFoundError:
        print()
        print("As this is your first time loading this application a new 'Note.txt' file will be generated")
        print()






print("NotePad!")
print("*" * 10)
print("Please enter 'v' to view all notes")
print("Please enter 'E' to edit a note")
print("Please enter 'D' to delete a specified note")

notes = []
read_notes(notes)


while True:
    print(notes)

    choice = input()