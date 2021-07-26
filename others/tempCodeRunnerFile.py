import math

a = int(input("Enter the starting number: "))
b = int(input("Enter the ending number: "))


def isPrime(num):
    if num > 1:
        count = 0
        for i in range(2, math.floor(math.sqrt(num))+1):
            if num % i == 0:
                count += 1

        if count >= 1:
            return False
        else:
            return True

    else:
        return False


for i in range(a, b+1):
    if(isPrime(i)):
        print(i)
