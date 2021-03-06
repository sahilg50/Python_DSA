# Insertion Sort Using Recursion

class InsertionSort:

    def __init__(self, array):
        self.array = array
        self.length = len(array)

    def __str__(self):
        return " ".join([str(item) for item in self.array])

    def insertionSortRecursive(self, i=1):

        # Base Case
        if i == self.length:
            return

        key = self.array[i]
        a = i-1

        while(a >= 0 and key < self.array[a]):
            self.array[a+1] = self.array[a]
            a -= 1

        self.array[a+1] = key

        self.insertionSortRecursive(i=i+1)


def main():

    # INtialize the array
    try:
        array = []
        while(True):
            array.append(int(input("Enter the Element: ")))

    except ValueError:
        print(array)

    # Initialize the object and then call the recursive sort function
    sort = InsertionSort(array=array)
    sort.insertionSortRecursive()
    print('The sorted array is :\n', sort)


if __name__ == '__main__':
    main()
