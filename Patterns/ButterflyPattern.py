rows = int(input("Enter the number of rows: "))

for i in range(1, rows+1):
    for j in range(i):
        print("*", end=" ")
    for k in range(rows-i):
        print(" ", end=" ")

    for k in range(rows-i):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")

    print("")

for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end=" ")
    for k in range(rows-i):
        print(" ", end=" ")

    for k in range(rows-i):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")

    print("")
