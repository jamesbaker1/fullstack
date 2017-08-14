def binaryString(bString, tempString = ''):
    if len(bString) == 0:
        print(tempString)
    else:
        if bString[0] == 'X':
            binaryString(bString[1:], tempString + '0')
            binaryString(bString[1:], tempString + '1')
        else:
            binaryString(bString[1:], tempString + bString[0])

# O(2^w) where w is the amount of Xs in the string
