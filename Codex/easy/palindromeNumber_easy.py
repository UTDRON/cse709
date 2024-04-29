'''
Given an integer x, return true if x is a 
palindrome
, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-2^31 <= x <= 2^31 - 1
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x < 10:
            return True
        else:
            return str(x) == str(x)[::-1]


import sys

if len(sys.argv) < 2:
    num_simulations = 1
else:
    if sys.argv[1] == "1":
        num_simulations = 1
    else:
        num_simulations = 10000000

for _ in range(num_simulations):
    input_x = 121
    Solution().isPalindrome(input_x)
    input_x = -121
    Solution().isPalindrome(input_x)
    input_x = 10
    Solution().isPalindrome(input_x)
    input_x = 123456789987654321
    Solution().isPalindrome(input_x)


# input_x = 121
# print(Solution().isPalindrome(input_x))
# input_x = -121
# print(Solution().isPalindrome(input_x))
# input_x = 10
# print(Solution().isPalindrome(input_x))
# input_x = 123456789987654321
# print(Solution().isPalindrome(input_x))