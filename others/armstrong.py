import math

num = int(input("Enter the number to be checked: "))

original = num
sum = 0
while num > 0:
    lastDigit = num % 10
    sum += math.pow(lastDigit, 3)
    num = math.floor(num/10)

if(sum == original):
    print("The number is armstrong! ")
else:
    print("The number is not armstrong! ")
