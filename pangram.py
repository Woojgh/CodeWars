import string
'''This function will tell you if a sentence is a Pangram.'''


def is_pan(sentence):
    checklist = []
    for letter in sentence.lower():
        if letter not in checklist:
            if letter.isalpha() is True:
                checklist.append(letter)
                if checklist == list(string.ascii_lowercase):
                    print('Is Pangram!')
