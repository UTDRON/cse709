'''
The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

 

Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
Example 3:

Input: n = 3, k = 1
Output: "123"
 

Constraints:

1 <= n <= 9
1 <= k <= n!
'''
import math

def getPermutation(n: int, k: int) -> str:
    nums = [str(i) for i in range(1, n+1)]
    result = ""
    k -= 1  # Convert k to 0-based index
    
    # Calculate factorial of n
    factorial = math.factorial(n)
    
    for i in range(n):
        # Calculate index of the current digit to select
        factorial //= (n - i)
        index = k // factorial
        
        # Append selected digit to result and remove it from the list
        result += nums.pop(index)
        
        # Update k for next iteration
        k %= factorial
    
    return result

# Example usage:
print(getPermutation(3, 3))  # Output: "213"
print(getPermutation(4, 9))  # Output: "2314"
print(getPermutation(3, 1))  # Output: "123"
