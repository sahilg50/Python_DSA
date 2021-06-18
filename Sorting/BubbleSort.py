# Bubble Sort

def sort(array):

    for i in range(len(array)):

        for j in range(0, len(array)-1-i):

            if(array[j] > array[j+1]):
                array[j], array[j+1] = array[j+1], array[j]

    print(array)


def main():

    # Create an array
    array = []
    try:
        while(True):
            array.append(int(input("Enter the Element: ")))

    except ValueError:
        print(array)

    if(len(array) != 0):
        sort(array=array)
    else:
        print("The array is empty!")


if __name__ == '__main__':
    main()
