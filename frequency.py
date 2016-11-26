import sys


def frequency(given_text):
    freqTable = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [10, 0], [11, 0],
                 [12, 0], [13, 0], [14, 0], [15, 0], [16, 0], [17, 0], [18, 0], [19, 0], [20, 0], [21, 0], [22, 0],
                 [23, 0], [24, 0], [25, 0], [26, 0]]  # table for storing [letter,frequency]

    given_text = given_text.lower()  # flips all str to lower case
    index = 0
    while (index < (len(given_text))):
        value = (ord(given_text[index])) - 97  # value is the letter location is freqTable
        if (value >= 0 and value <= 26):
            freqTable[value][1] = freqTable[value][1] + 1  # increment if it is a letter
        else:
            freqTable[26][1] += 1  # incrament is it is a space
        index = index + 1

    freqTable = (sorted(freqTable, key=lambda t: t[1], reverse=True))  # sort table based on most frequent
    index = 0
    while (index < 26):
        if ((freqTable[index][0]) <= 25 and (freqTable[index][0]) >= 0):  # print out table
            print (chr((freqTable[index][0]) + 97)).upper(), ":", freqTable[index][1]
            index = index + 1
        else:
            index += 1


givenText = ''.join(sys.argv[1:])  # input from command line
frequency(givenText)  # call main function

# frequency("inixepfcr ipc xipfvcr cepc pki ginaqadvr")                       #just so i wouldnt lose it
# frequency("ELEPHANTS EAT PEANUTS THAT ARE DELICIOUS")                       #just so i wouldnt lose it
