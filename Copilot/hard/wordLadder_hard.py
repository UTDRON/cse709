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

def ladderLength(beginWord, endWord, wordList):
    # Create a set for faster lookup
    wordSet = set(wordList)
    
    # If endWord is not in wordList, return 0
    if endWord not in wordSet:
        return 0
    
    # Initialize the queue with beginWord and its level
    queue = deque([(beginWord, 1)])
    
    # Perform BFS
    while queue:
        word, level = queue.popleft()
        
        # Check if we have reached the endWord
        if word == endWord:
            return level
        
        # Generate all possible next words by changing one letter at a time
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                nextWord = word[:i] + c + word[i+1:]
                
                # If the nextWord is in wordSet, add it to the queue and remove it from wordSet
                if nextWord in wordSet:
                    queue.append((nextWord, level + 1))
                    wordSet.remove(nextWord)
    
    # If no transformation sequence exists, return 0
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