def is_palindrome(string):  # method for singular word
    return string[::-1].casefold() == string.casefold()


def is_palindrome_sentence(sentence):  # method for sentence, overcoming spaces and punctuation
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    print(string)
    return string[::-1].casefold() == string.casefold()


def diff_palindrome_sentence(sentence):
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


# if is_palindrome(word):
#     print("'{}' is a palindrome".format(word))
# else:
#     print("'{}' is not a palindrome".format(word))

# if is_palindrome_sentence(word):
#     print("'{}' is a palindrome".format(word))
# else:
#     print("'{}' is not a palindrome".format(word))
