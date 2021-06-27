# Given two strings. The task is to find the length of the longest common substring.

def LCSubStr_iterative():
    """
    Using simple iteration
    """
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")
    m = len(str1)
    n = len(str2)

    LCSuff = [[0 for i in range(n+1)] for j in range(m+1)]

    result = 0

    for i in range(m+1):
        for j in range(n+1):
            if(i == 0 or j == 0):
                LCSuff[i][j] = 0
            elif(str1[i-1] == str2[j-1]):
                LCSuff[i][j] = LCSuff[i-1][j-1]+1
                result = max(result, LCSuff[i][j])
            else:
                LCSuff[i][j] = 0

    return result


class Strings():

    def __init__(self):
        self.str1 = input("Enter the first string: ")
        self.str2 = input("Enter the second string: ")

    def LCSubStr_recurive(self, i=None, j=None, count=0):
        """
        Using Recursion
        """
        if(i == None):
            i = len(self.str1)
            j = len(self.str2)

        # Base Case
        if (i == 0 or j == 0):
            return count

        elif(self.str1[i-1] == self.str2[j-1]):
            count = self.LCSubStr_recurive(i-1, j-1, count+1)

        else:
            count = max(count, max(self.LCSubStr_recurive(
                i, j-1, 0), self.LCSubStr_recurive(i-1, j, 0)))

        return count


def main():

    strings = Strings()
    print(strings.LCSubStr_recurive())


if __name__ == '__main__':
    main()
