# Merge Sort

class MergeSort:
    """
     MergeSort:
          function:
              bubbleSortRecursive : recursive
                  function to sort array
              __str__ : format print of array
              __init__ : constructor
                  function in python
          variables:
              self.array = contains array
              self.length = length of array
    """

    def __init__(self, array):
        self.array = array
        self.length = len(array)
        self.counter = 0

    def __str__(self):
        return str(self.counter)

    def MergeSortRecursion(self, array=None):

        if array is None:
            array = self.array

        # Base Case
        if len(array) > 1:

            # Finding the middle element
            mid = len(array)//2

            # Dividing the Array elements into 2 Halves
            L = array[:mid]

            R = array[mid:]

            # Sorting Both the halves
            self.MergeSortRecursion(L)
            self.MergeSortRecursion(R)

            i = j = k = 0

            # Copy data from temporary arrays L[] and R[]
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    array[k] = L[i]
                    i += 1
                else:
                    array[k] = R[j]
                    j += 1
                k += 1
                self.counter += 1

            # Checking and Coping the remaining variables.
            while i < len(L):
                array[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                array[k] = R[j]
                j += 1
                k += 1


def main():

    # Initialize the array
    try:
        array = []
        while(True):
            array.append(int(input("Enter the Element: ")))

    except ValueError:
        print(array)

    Sort = MergeSort(array=array)
    Sort.MergeSortRecursion()
    print("The sorted array is: ", Sort)


if __name__ == '__main__':
    main()
