# Selection sort using Recursion

class SelectionSort:

    def __init__(self, array):
        self.array = array
        self.length = len(array)

    def __str__(self):
        return " ".join([str(item) for item in self.array])

    def selectionSortRecurcive(self, i=0):

        # Base Case
        if i == self.length-1:
            return

        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i+1, self.length):
            if self.array[min_idx] > self.array[j]:
                min_idx = j

        # Swap the found minimum element with
        # the first element
        self.array[min_idx], self.array[i] = self.array[i], self.array[min_idx]

        i += 1
        self.selectionSortRecurcive(i=i)


def main():

    # Initialize the array
    array = []
    try:
        while(True):
            array.append(int(input("Enter the element: ")))

    except ValueError:
        print(array)

    if(len(array) != 0):
        sort = SelectionSort(array=array)
        sort.selectionSortRecurcive()
        print("The sorted array is :\n", sort)
    else:
        print("The array is empty")


# Driver Code
if __name__ == '__main__':
    main()
