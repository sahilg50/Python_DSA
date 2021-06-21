# Insertion sort

def insertionSort(array):

    length = len(array)

    if(length == 0):
        print("The Array is empty!")
        return

    for i in range(1, length):

        key = array[i]
        a = i-1
        while(a >= 0 and key < array[a]):
            array[a+1] = array[a]
            a -= 1
        array[a+1] = key

    return array


def main():

    # Initialize the Array
    try:
        array = []
        while(True):
            array.append(int(input("Enter the element: ")))

    except ValueError:
        print(array)

    print(insertionSort(array=array))


if __name__ == '__main__':
    main()
