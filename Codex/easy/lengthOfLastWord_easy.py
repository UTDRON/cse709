'''
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal 
substring
 consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
 

Constraints:

1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.
'''
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Remove trailing spaces
        s = s.rstrip()
        
        # Initialize the length of the last word
        length = 0
        
        # Iterate from the end of the string
        for i in range(len(s) - 1, -1, -1):
            # If we encounter a space, break the loop
            if s[i] == ' ':
                break
            # Increment the length of the last word
            length += 1
        
        # Return the length of the last word
        return length

# Test cases
sol = Solution()
print(sol.lengthOfLastWord("Hello World"))  # Output: 5
print(sol.lengthOfLastWord("   fly me   to   the moon  "))  # Output: 4
print(sol.lengthOfLastWord("luffy is still joyboy"))  # Output: 6