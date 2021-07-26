num = int(input("Enter the number to be checked: "))


def Check_Prime(num):
    if num < 2:
        print("The number is not prime! ")

    else:
        for i in range(2, num):
            if(num % i == 0):
                return print("prime")

            return print("Non Prime")


Check_Prime(num)
