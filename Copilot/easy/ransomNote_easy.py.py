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
def canConstruct(ransomNote: str, magazine: str) -> bool:
        ransomNote_dict = {}
        magazine_dict = {}
        
        # Count the frequency of each letter in ransomNote
        for char in ransomNote:
            if char in ransomNote_dict:
                ransomNote_dict[char] += 1
            else:
                ransomNote_dict[char] = 1
        
        # Count the frequency of each letter in magazine
        for char in magazine:
            if char in magazine_dict:
                magazine_dict[char] += 1
            else:
                magazine_dict[char] = 1
        
        # Check if ransomNote can be constructed using letters from magazine
        for char, count in ransomNote_dict.items():
            if char not in magazine_dict or count > magazine_dict[char]:
                return False
        
        return True

# Test cases
print(canConstruct("a", "b"))    # Output: False
print(canConstruct("aa", "ab"))   # Output: False
print(canConstruct("aa", "aab"))  # Output: True