def main():
    # Initialize the Array
    try:
        array = []
        while(True):
            array.append(int(input("Enter the element: ")))

    except ValueError:
        print(array)

    hashmap = {}
    for i in range(len(array)):
        if array[i] in hashmap:
            hashmap[array[i]] += 1
        else:
            hashmap[array[i]] = 1

    print(hashmap)


if __name__ == '__main__':
    # Call the main function
    main()
