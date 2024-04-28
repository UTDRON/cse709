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
        # Remove leading and trailing spaces
        s = s.strip()
        
        # Find the last space in the string
        last_space_index = s.rfind(' ')
        
        # If there is no space, return the length of the entire string
        if last_space_index == -1:
            return len(s)
        
        # Return the length of the last word
        return len(s[last_space_index+1:])

# Test cases
sol = Solution()
print(sol.lengthOfLastWord("Hello World"))  # Output: 5
print(sol.lengthOfLastWord("   fly me   to   the moon  "))  # Output: 4
print(sol.lengthOfLastWord("luffy is still joyboy"))  # Output: 6