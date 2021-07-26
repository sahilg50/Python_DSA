rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))


def fact(num):

    if(num == 0 or num == 1):
        return 1

    factorial = 1
    for i in range(2, num+1):
        factorial *= i
    return factorial


def nCr(n, r):

    answer = fact(n)/((fact(n-r))*(fact(r)))
    return answer


for i in range(rows):
    for j in range(i+1):
        print(int(nCr(i, j)), end=" ")
    print("")
