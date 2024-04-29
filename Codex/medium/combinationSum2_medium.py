'''
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
 

Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
'''
def combinationSum2(candidates, target):
    def backtrack(start, target, path):
        if target == 0:
            result.append(path)
            return
        if target < 0:
            return
        
        for i in range(start, len(candidates)):
            # Skip duplicates
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            backtrack(i + 1, target - candidates[i], path + [candidates[i]])
    
    candidates.sort()  # Sort the candidates to handle duplicates
    result = []
    backtrack(0, target, [])
    return result

# Example usage:
import sys

if len(sys.argv) < 2:
    num_simulations = 1
else:
    if sys.argv[1] == "1":
        num_simulations = 1
    else:
        num_simulations = 1000000

for _ in range(num_simulations):
    candidates1 = [10, 1, 2, 7, 6, 1, 5]
    target1 = 8
    combinationSum2(candidates1, target1)

    candidates2 = [2, 5, 2, 1, 2]
    target2 = 5
    combinationSum2(candidates2, target2)



# candidates1 = [10, 1, 2, 7, 6, 1, 5]
# target1 = 8
# print(combinationSum2(candidates1, target1))
# # Output: [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]

# candidates2 = [2, 5, 2, 1, 2]
# target2 = 5
# print(combinationSum2(candidates2, target2))
# # Output: [[1, 2, 2], [5]]