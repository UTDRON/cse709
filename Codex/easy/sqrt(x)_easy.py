'''
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
 

Constraints:

0 <= x <= 231 - 1

'''
def mySqrt(x: int) -> int:
    # Handle edge cases
    if x == 0:
        return 0
    if x == 1:
        return 1
    
    # Initialize the left and right pointers for binary search
    left = 1
    right = x // 2
    
    # Perform binary search
    while left <= right:
        mid = left + (right - left) // 2
        square = mid * mid
        
        # If the square of mid is equal to x, return mid
        if square == x:
            return mid
        # If the square of mid is greater than x, move right pointer to mid - 1
        elif square > x:
            right = mid - 1
        # If the square of mid is less than x, move left pointer to mid + 1
        else:
            left = mid + 1
    
    # When the loop ends, left pointer will be greater than right pointer
    # So, return right pointer (the rounded down square root)
    return right

# Test cases
import sys

if len(sys.argv) < 2:
    num_simulations = 1
else:
    if sys.argv[1] == "1":
        num_simulations = 1
    else:
        num_simulations = 10000000

for _ in range(num_simulations):
    mySqrt(4)  # Output: 2
    mySqrt(8)  # Output: 2

# print(mySqrt(4))  # Output: 2
# print(mySqrt(8))  # Output: 2