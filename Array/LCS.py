# Given two strings. The task is to find out the longest common subsequence.

"""
Examples:
LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.
LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.
"""

# To improve the results of recursion we can use the process of memoization


class Strings:

    def __init__(self):
        self.str1 = input("Enter the first string: ")
        self.str2 = input("Enter the secong string: ")

    def LCS(self, i=0, j=0):

        # Base Case
        if(i >= len(self.str1) or j >= len(self.str2)):
            return 0

        # if equal, then we store the value of the function call
        elif(self.str1[i] == self.str2[j]):
            return 1 + self.LCS(i+1, j+1)

        else:
            return max(
                self.LCS(i+1, j), self.LCS(i, j+1))


def main():
    strings = Strings()
    print(strings.LCS())


if __name__ == "__main__":
    main()
