import math
num = int(input("Enter the number to be reversed: "))

reverse = 0

while(num > 0):
    last_digit = num % 10
    reverse = reverse*10 + last_digit
    num = math.floor(num / 10)


print(reverse)
