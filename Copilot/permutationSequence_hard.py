
'''
The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

 

Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
Example 3:

Input: n = 3, k = 1
Output: "123"
 

Constraints:

1 <= n <= 9
1 <= k <= n!
'''

def getPermutation(n, k):
    def backtrack(nums, path):
        if len(path) == n:
            permutations.append(path[:])
            return
        for num in nums:
            if num not in path:
                path.append(num)
                backtrack(nums, path)
                path.pop()

    nums = [str(i) for i in range(1, n+1)]
    permutations = []
    backtrack(nums, [])
    permutations.sort()
    return ''.join(permutations[k-1])

n = 3
k = 3
print(getPermutation(n, k))  # Output: "213"

n = 4
k = 9
print(getPermutation(n, k))  # Output: "2314"

n = 3
k = 1
print(getPermutation(n, k))  # Output: "123"