# Sean Holmes
import sys

def encrypt(givenText, givenRotation):
    cipherText = ""  # encrypted text     //string
    givenText = givenText.lower()  # get given text to lowercase
    # initialize loop
    index = 0  # index in given string
    while index < (len(givenText)):  # begin encrypting
        value = (ord(givenText[index])) + givenRotation  # use unicode value and rotate to given rotation
        if (value <= 122 and value >= 97):  # if the value is in range a to z
            cipherText = cipherText + chr(value)  # add char to cipher text
        elif (value >= 123):  # if the value is above a-z
            cipherText = cipherText + chr(value - 26)  # bring it back down to range and add to text
        else:  # any other value not in a-z will be treated as ' '
            cipherText = cipherText + " "
        index = index + 1  # increment to next char

    print(cipherText)  # output encrypted text


def decrypt(givenText, givenRotation):
    cipherText = ""  # encrypted text     //string
    givenText = givenText.lower()  # get given text to lowercase
    # initialize loop
    index = 0  # index in given string
    while index < (len(givenText)):  # begin encrypting
        value = (ord(givenText[index])) - givenRotation  # rotate to given rotation
        if (value <= 122 and value >= 97):  # if the value is in range a to z
            cipherText = cipherText + chr(value)  # decrypt and add to text
        elif (value <= 97 and value >= 56):  # if the value is below a-z
            cipherText = cipherText + chr(value + 26)  # bring it back down to range and add to text
        else:  # any other value not in a-z will be treated as ' '
            cipherText = cipherText + " "

        index = index + 1  # increment to next char

    print(cipherText)  # output decrypted text


def decryptBrute(givenText):
    index = 25  # 26 total loops
    while (index != 0):
        decrypt(givenText, index)
        index = index - 1


argList = sys.argv
# Mode: -e , -u , -d


if (argList[1] == '-e'):  # Encrypt with rotation
    encrypt(' '.join(argList[3:]), int(argList[2]))
elif (argList[1] == '-u'):  # Decrypt with rotation
    decrypt(' '.join(argList[3:]), int(argList[2]))
elif (argList[1] == '-d'):  # Brute force decrypt
    decryptBrute(' '.join(argList[2:]))
else:
    print("Please enter -e -u  or -d")
