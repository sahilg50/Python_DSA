#Function to reverse the array
def reverse(array):
        
        if(len(array)==0):
            return ("The array is empty!")
        
        L = 0
        R = len(array)-1

        while(L!=R and L<R):
            array[R], array[L] = array[L], array[R]
            L+=1
            R-=1

        return array

#Main Function
def main():
    array = []
    
    lenght = int(input('Enter the size of the array: '))

    for i in range(lenght):
        while(True):
            try:
                element = int(input('Enter the {} element: '.format(i+1)))
                array.append(element)
                break
            except(ValueError):
                print("Oops! Please enter a numebr.")
    
    print(reverse(array))




if __name__ == "__main__": 
    main()