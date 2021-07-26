n = int(input("Enter the length of series: "))

term1 = 0
term2 = 1
nextTerm = 0
print(term1)
print(term2)
for i in range(n-2):
    nextTerm = term1+term2
    print(nextTerm)
    term1, term2 = term2, nextTerm
