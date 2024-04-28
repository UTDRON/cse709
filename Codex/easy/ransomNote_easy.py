'''
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
'''
from collections import Counter
def canConstruct( ransomNote: str, magazine: str) -> bool:
        # Count the frequency of each letter in ransomNote and magazine
        ransom_freq = Counter(ransomNote)
        magazine_freq = Counter(magazine)
        
        # Check if the frequency of each letter in ransomNote is less than or equal to the frequency in magazine
        for letter, freq in ransom_freq.items():
            if freq > magazine_freq[letter]:
                return False
        
        # If all letters in ransomNote can be constructed from magazine, return True
        return True

# Test cases
print(canConstruct("a", "b"))    # Output: False
print(canConstruct("aa", "ab"))   # Output: False
print(canConstruct("aa", "aab"))  # Output: True