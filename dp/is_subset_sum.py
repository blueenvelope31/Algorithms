"""
Problem: https://en.wikipedia.org/wiki/Subset_sum_problem

Given a set of integers, is there a non-empty subset whose sum is zero?

>>> isSubsetSum([2, 4, 15, 11, 8], 34)
True
>>> isSubsetSum([2, 4, 15, 11, 8], 35)
False
>>> isSubsetSumRecursive([2, 4, 15, 11, 8], 34)
True
>>> isSubsetSumRecursive([2, 4, 15, 11, 8], 35)
False
"""

def isSubsetSum(s, total):
    """Returns true if there is a subset of s with sum total else false""" 
    return isSubsetSumHelper(s, len(s), total)


def isSubsetSumHelper(s, n, total):
    """Helper function for dynamic programming implementation""" 

    # The value of subset[i][j] will be true if there is a 
    # subset of s[0..j-1] with sum equal to i 
    subset = []
    # If sum is 0, then answer is true 
    for i in range(n + 1):
        subset.append([True])
   
    # If sum is not 0 and set is empty, then answer is false 
    for i in range(1, total + 1): 
      subset[0].append(False) 
   
    # Fill the subset table in botton up manner 
    for i in range(1, n + 1): 
        for j in range(1, total + 1): 
            if j < s[i-1]: 
                subset[i].append(subset[i-1][j]) 
            if j >= s[i-1]: 
                subset[i].append(subset[i-1][j] or subset[i - 1][j-s[i-1]])
    return subset[n][total]


def isSubsetSumRecursive(s, total):
    """Returns true if there is a subset of s with sum total else false"""
    return isSubsetSumRecursiveHelper(s, len(s), total)


def isSubsetSumRecursiveHelper(s, n, total): 
    """Helper function for recursive implentation"""
    # Base Cases
    if (total == 0) : 
        return True
    if (n == 0 and total != 0) : 
        return False
   
    # If last element is greater than total, then ignore it 
    if (s[n - 1] > total) : 
        return isSubsetSumRecursiveHelper(s, n - 1, total); 
   
    # else, check if total can be obtained by any of the following 
    # (a) including the last element 
    # (b) excluding the last element    
    return isSubsetSumRecursiveHelper(s, n-1, total) or isSubsetSumRecursiveHelper(s, n-1, total-s[n-1])
