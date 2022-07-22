def diff_palindrome_sentence(sentence):
    """
   Get a String from Standard Input (stdin) to ascertain whether
   the String is a palindrome.

   The function will first strip the punctuation and spaces from the string.
   Assigning the cleansed string to the variable string

   It will then create the variable "num_checks", this variable is assigned
   the length of the string divided by 2. As we're checking for a palindrome
   we do not require half the characters tested.
   The 'I' variable is assigned for matching the first index character of the
   String with the last character being assigned to 'J'.

   It will then loop to compare the letters whilst incrementing 'i' &
   decrementing 'j' until it reaches the middle character (num_checks value)

   :param sentence: The sentence to check.

   :return: True or False whether the entered 'String' is a
       Palindrome
   """
    string = ""
    # variable to remove spaces/punctuation

    for char in sentence:
        if char.isalnum():
            string += char.casefold()

    num_checks = int(len(string) / 2)
    # number of loops for it to compare the first indexed character with the last
    j = int(len(string)) - 1
    # index of the last character
    # number of loops for it to compare the first indexed character with the last
    i = 0
    # first character index

    for letter in range(0, num_checks):
        if string[i] != string[j]:
            return False
        else:
            i += 1
            j -= 1
    if i == num_checks:
        return True


word = input("Please enter a word to check: ")

if diff_palindrome_sentence(word):
    print("'{}' is a palindrome".format(word))
else:
    print("'{}' is not a palindrome".format(word))

