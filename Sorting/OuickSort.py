# QuickSort Algorithm

class Quicksort:

    # Constructor
    def __init__(self, array):
        self.array = array
        self.length = len(array)

    # This method is called when the print command is called
    def __str__(self):
        return " ".join([str(item) for item in self.array])

    # Method for swaping the elements
    def Swap(self, a, b):

        self.array[a], self.array[b] = self.array[b], self.array[a]

    # Method for partitioning the array using pivot
    def partition(self, l, r):

        pivot = self.array[r]

        i = l-1

        for j in range(l, r):
            if self.array[j] < pivot:
                i += 1
                self.Swap(i, j)

        self.Swap(i+1, r)

        return i+1

    # Quicksort method (Rescursive Approach)
    def quickSort(self, l=None, r=None):
        if(l is None and r is None):
            l = 0
            r = self.length-1

        if(l < r):
            pi = self.partition(l, r)

            self.quickSort(pi+1, r)
            self.quickSort(l, pi-1)


def main():
    # Initialize the Array
    try:
        array = []
        while(True):
            array.append(int(input("Enter the element: ")))

    except ValueError:
        print(array)

    # Create the object and call the quicksort method
    sort = Quicksort(array=array)
    sort.quickSort()
    print("The sorted array is: ", sort)


if __name__ == '__main__':
    # Call the main function
    main()
