# A Dynamic Programming based Python
# Program for 0-1 Knapsack problem
# Returns the maximum value that can
# be put in a knapsack of capacity W

def knapsack_dp(items, max_weight):
    n = len(items)
    K = [[0 for _ in range(max_weight + 1)] for _ in range(n + 1)]

    # split the items into two lists
    val = [item[0] for item in items]
    wt = [item[1] for item in items]

    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(max_weight + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1]
                              + K[i-1][w-wt[i-1]],
                              K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
 
    return K[n][max_weight]
 

if __name__ == '__main__':

    # Driver program to test above function
    items = [(60, 10), (100, 20), (120, 30)]
    max_weight = 50
    n = len(items)

    result = knapsack_dp(items, max_weight)
    assert result == 220
    print(result)

# Time Complexity: O(N * W). where ‘N’ is the number of elements and ‘W’ is capacity.
# Auxiliary Space: O(N * W). The use of a 2-D array of size ‘N*W’.
 
# This code is contributed by Bhavya Jain, tweaked by me to work with my data structure
# https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
