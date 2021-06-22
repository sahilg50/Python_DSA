# Find the maximum and minimum element in an array

def get_min_max(low, high, array):
    """
    (Tournament Method)  Recursive method to get min max.
    Divide the array into two parts and compare the maximums and minimums of the two parts to get the maximum and the minimum of the whole array.
    """

    # If array has only one element
    if(low == high):
        array_min = array[low]
        array_max = array[high]
        return(array_min, array_max)

    # If array has only two elements
    elif(high == low+1):
        a = array[low]
        b = array[high]
        if(a > b):
            array_max = a
            array_min = b
        else:
            array_max = b
            array_min = a
        return (array_max, array_min)

    else:
        mid = int((low + high) / 2)
        arr_max1, arr_min1 = get_min_max(low, mid, array)
        arr_max2, arr_min2 = get_min_max(mid + 1, high, array)

    return (max(arr_max1, arr_max2), min(arr_min1, arr_min2))


def main():

    # Create an array
    array = []
    try:
        while True:
            array.append(int(input("Enter the element: ")))

    except ValueError:
        print(array)

    if(len(array) == 0):
        print('The array is empty!')
        return

    low = 0
    high = len(array) - 1

    arr_max, arr_min = get_min_max(low, high, array)
    print('Minimum element is ', arr_min)
    print('nMaximum element is ', arr_max)


if __name__ == "__main__":
    main()
