num = int(input("Enter the number whose factorial is to be calculated: "))


def fact(num):

    if(num == 0 or num == 1):
        return print(1)

    factorial = 1
    for i in range(2, num+1):
        factorial *= i
    return print(factorial)


fact(num)
