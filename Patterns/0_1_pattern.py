rows = int(input("Enter the number of rows: "))

for i in range(1, rows+1):
    for j in range(i):
        if(i+j+1) % 2 == 0:
            print(1, end=" ")
        else:
            print(0, end=" ")

    print("")
