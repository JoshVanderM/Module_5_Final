import math

def radianCovert():
    value = float(input("Please type the value to be converted:  "))
    type = input("type what the type of number you typed above was\n'd' or 'D' for degree 'r' or 'R' for radians:  ")
    if (type == "d" or type == "D"):
        final = value * (math.pi / 180)
        print(f"your value in radians is: {final}")
    else:
        final = value * (180 / math.pi)
        print(f"your value in degrees is: {final}")


def sortList( list, str ):
    if( str == 'asc' ):
        list = list.sort()
    elif(str == "desc" ):
        list = list.sort(reverse=True)
    print(list)

def decimalCovert( value ):
    print( value.bin() )

def vowelCount( string ):
    vowels = "aeiouAEIOU"
    numVowels = 0
    for letter in string:
        if letter in vowels:
            numVowels += 1
    print( numVowels )

def hideCardNum( cardNum ):
    cardNum = str(cardNum)
    for i in range(3):
        print("X"*4+" ", end="")
    print(cardNum[12:])

def countXO( string ):
    countX = 0
    countO = 0
    for item in string:
        if item in "xX":
            countX += 1
        elif item in "oO":
            countO += 1
    return countX == countO

def calculator(intOne, operator, intTwo):
    if operator == "+":
        return intOne + intTwo
    elif operator == "-":
        return intOne - intTwo
    elif operator == "*":
        return intOne * intTwo
    else:
        return intOne // intTwo

def calculateDiscount( price, discount ):
    return price * ((100 - discount) / 100)

def justNumbers( list ):
    numList = []
    for items in list:
        if isinstance(items, float) or isinstance(items, int):
            numList.append(items)
    print(numList)

def repeatChar( string ):
    returnString = ""
    for items in string:
        returnString += (items * 2)

    print(returnString)
