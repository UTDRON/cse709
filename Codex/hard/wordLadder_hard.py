'''
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

 

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
 

Constraints:

1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.
'''
from collections import deque

def ladderLength(beginWord: str, endWord: str, wordList: list[str]) -> int:
    # Convert wordList to a set for faster lookup
    wordSet = set(wordList)
    
    if endWord not in wordSet:
        return 0
    
    queue = deque([(beginWord, 1)])  # Initialize queue with (word, level)
    visited = set([beginWord])
    
    while queue:
        word, level = queue.popleft()
        if word == endWord:
            return level
        
        for i in range(len(word)):
            for char in 'abcdefghijklmnopqrstuvwxyz':
                new_word = word[:i] + char + word[i+1:]
                if new_word in wordSet and new_word not in visited:
                    visited.add(new_word)
                    queue.append((new_word, level + 1))
    
    return 0

# Example usage:
import sys

if len(sys.argv) < 2:
    num_simulations = 1
else:
    if sys.argv[1] == "1":
        num_simulations = 1
    else:
        num_simulations = 100000

for _ in range(num_simulations):
    beginWord1 = "hit"
    endWord1 = "cog"
    wordList1 = ["hot","dot","dog","lot","log","cog"]
    ladderLength(beginWord1, endWord1, wordList1)  # Output: 5

    beginWord2 = "hit"
    endWord2 = "cog"
    wordList2 = ["hot","dot","dog","lot","log"]
    ladderLength(beginWord2, endWord2, wordList2)  # Output: 0

# beginWord1 = "hit"
# endWord1 = "cog"
# wordList1 = ["hot","dot","dog","lot","log","cog"]
# print(ladderLength(beginWord1, endWord1, wordList1))  # Output: 5

# beginWord2 = "hit"
# endWord2 = "cog"
# wordList2 = ["hot","dot","dog","lot","log"]
# print(ladderLength(beginWord2, endWord2, wordList2))  # Output: 0
