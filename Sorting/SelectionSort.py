# Selection Sort

def sort(array):

    for i in range(len(array)-1):

        min_idx = i
        for j in range(i+1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j

        array[min_idx], array[i] = array[i], array[min_idx]

    print(array)


def main():

    # Create an array
    array = []
    try:
        while(True):
            array.append(int(input("Enter the element: ")))
    except ValueError:
        print(array)

    if(len(array) != 0):
        sort(array=array)
    else:
        print('The array is empty')


if __name__ == '__main__':
    main()
