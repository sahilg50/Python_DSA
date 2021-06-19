# Bubble Sort Using Recursion.

class bubbleSort:
    """
     bubbleSort:
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

    # this function is called automatically whenever print() or str() command is called on the class.
    def __str__(self):
        return " ".join([str(x)
                        for x in self.array])

    def bubbleSortRecursive(self, n=None):
        if n is None:
            n = self.length

        # Base Case
        if n == 1:
            return

        # One pass of bubble sort. After
        # this pass, the largest element
        # is moved (or bubbled) to end.

        for i in range(n-1):
            if self.array[i] > self.array[i+1]:
                self.array[i], self.array[i+1] = self.array[i+1], self.array[i]

        # Largest element is fixed,
        #  recur for remaining array
        self.bubbleSortRecursive(n - 1)


def main():
    # Create Array
    try:
        array = []
        while(True):
            array.append(int(input("Enter the element: ")))

    except ValueError:
        print(array)

    if(len(array) != 0):

        # Creating object for class
        sort = bubbleSort(array)

        # Sorting array
        sort.bubbleSortRecursive()
        print("Sorted array :\n", sort)

    else:
        print("The Array is empty!")


if __name__ == '__main__':
    main()
