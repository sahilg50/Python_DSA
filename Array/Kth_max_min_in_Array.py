# Given an array and a number k where k is smaller than the size of the array, we need to find the k’th smallest element in the given array. It is given that all array elements are distinct.

def kthSmallest(arr, l, r, k):

    # If k is smaller than number of
    # elements in array
    if (k > 0 and k <= len(arr)):

        # Partition the array around last
        # element and get position of pivot
        # element in sorted array
        pos = partition(arr, l, r)

        # If position is same as k
        if (pos == k - 1):
            return arr[pos]
        if (pos > k - 1):  # If position is more,
            # recur for left subarray
            return kthSmallest(arr, l, pos - 1, k)

        # Else recur for right subarray
        return kthSmallest(arr, pos + 1, r,
                           k)

    # If k is more than number of
    # elements in array
    return "OutOfBound"

# Standard partition process of QuickSort().
# It considers the last element as pivot and
# moves all smaller element to left of it
# and greater elements to right


def partition(arr, l, r):

    pivot = arr[r]
    i = l
    for j in range(l, r):
        if (arr[j] <= pivot):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i


# Driver Code
if __name__ == "__main__":

    arr = [12, 3, 5, 7, 4, 19, 26]
    n = len(arr)
    k = 7
    print("K'th smallest element is",
          kthSmallest(arr, 0, n - 1, k))
