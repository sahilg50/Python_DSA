"""
Given an array consisting of the cost of toys. Given an integer K depicting the amount of money available to purchase toys. Write a program to find the maximum number of toys one can buy with the amount K. 
Note: One can buy only 1 quantity of a particular toy.

Examples:  

Input:  N = 10, K =  50
        cost = { 1, 12, 5, 111, 200, 1000, 10, 9, 12, 15 }
Output: 6
Explanation: Toys with amount 1, 5, 9, 10, 12, and 12 
can be purchased resulting in a total amount of 49. Hence,
maximum number of toys is 6.

Input: N = 7, K = 50
       cost = { 1, 12, 5, 111, 200, 1000, 10 }
Output: 4 
"""

# Python 3 Program to maximize the
# number of toys with K amount

# This functions returns the required
# number of toys


def maximum_toys(cost, N, K):
    count = 0
    sum = 0

    # sort the cost array
    cost.sort(reverse=False)
    for i in range(0, N, 1):

        # Check if we can buy ith toy or not
        if (sum+cost[i] <= K):
            sum = sum + cost[i]
            # Increment the count variable
            count += 1

    return count


# Driver Code
if __name__ == '__main__':
    K = 50
    cost = [1, 12, 5, 111, 200,
            1000, 10, 9, 12, 15]
    N = len(cost)

    print(maximum_toys(cost, N, K))
