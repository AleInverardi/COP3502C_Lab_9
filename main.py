# Alessandro Inverardi encode fnc

def encode(password):
    EncodedList = []  # blank list for integers
    EncodedPassword = ''  # blank string for output
    for letter in range(len(password)):
        EncodedList += [(int(password[letter]) + 3) % 10]  # making a list of new integers

    for item in range(len(EncodedList)):
        EncodedPassword += str(EncodedList[item])  # change new list of integers to new string

    return EncodedPassword

