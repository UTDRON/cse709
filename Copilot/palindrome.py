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
        # Convert the integer to a string
        x_str = str(x)
        
        # Check if the string is equal to its reverse
        return x_str == x_str[::-1]


input_x = 121
print(Solution().isPalindrome(input_x))
input_x = -121
print(Solution().isPalindrome(input_x))
input_x = 10
print(Solution().isPalindrome(input_x))
input_x = 123456789987654321
print(Solution().isPalindrome(input_x))