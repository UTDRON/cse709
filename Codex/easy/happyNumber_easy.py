'''
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

 

Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
Example 2:

Input: n = 2
Output: false
 

Constraints:

1 <= n <= 231 - 1
'''

def isHappy(n: int) -> bool:
        # Set to store seen sums of squares of digits
        seen = set()
        
        # Iterate until n becomes 1 (happy) or enters a cycle
        while n != 1:
            # Calculate the sum of the squares of digits of n
            sum_of_squares = 0
            while n > 0:
                digit = n % 10
                sum_of_squares += digit ** 2
                n //= 10
            
            # If the sum is seen before, it's a cycle, return False
            if sum_of_squares in seen:
                return False
            
            # Add the current sum to the seen set
            seen.add(sum_of_squares)
            
            # Update n with the new sum
            n = sum_of_squares
        
        # If the loop ends with n = 1, it's a happy number
        return True

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
    isHappy(19)  # Output: True
    isHappy(2)   # Output: False

# print(isHappy(19))  # Output: True
# print(isHappy(2))   # Output: False