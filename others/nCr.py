# nCr is equal to n!/(n-r)!*r!

n = int(input("Enter the number whose factorial is to be calculated: "))

r = int(input("Enter the repetetion: "))


def fact(num):

    if(num == 0 or num == 1):
        return 1

    factorial = 1
    for i in range(2, num+1):
        factorial *= i
    return factorial


answer = fact(n)/((fact(n-r))*(fact(r)))
print(answer)
