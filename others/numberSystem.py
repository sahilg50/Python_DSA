import math


def BinToDec():

    num = int(input("Enter the number to be converted to decimal number: "))

    sum = 0
    x = 1

    while(num > 0):
        last_digit = num % 10
        sum += x*last_digit
        x *= 2
        num = math.floor(num/10)

    print(sum)


def OctToDec():

    num = int(input("Enter the number to be converted to decimal number: "))

    sum = 0
    x = 1

    while(num > 0):
        last_digit = num % 10
        sum += x*last_digit
        x *= 8
        num = math.floor(num/10)

    print(sum)


def HexToDec():

    num = input("Enter the number to be converted to the decimal number: ")

    ans = 0
    x = 1
    for i in range(len(num)-1, -1, -1):

        if(num[i] >= '0' and num[i] <= '9'):
            ans += x*(ord(num[i])-ord('0'))

        elif(num[i] >= 'A' and num[i] <= 'F'):
            ans += x*(ord(num[i])-ord('A') + 10)

        else:
            raise ValueError(
                'The number you entered is not a hexadecimal number! ')
        x *= 16
    print(ans)


def DecToBin():
    num = int(input("Enter the number that you want to convert to binary: "))

    x = 1
    ans = 0
    while(x <= n):
        x += 2


HexToDec()
