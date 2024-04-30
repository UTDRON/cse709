'''
You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.

If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.

 

Example 1:

Input: nums = [3,1,5,8]
Output: 167
Explanation:
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
Example 2:

Input: nums = [1,5]
Output: 10
 

Constraints:

n == nums.length
1 <= n <= 300
0 <= nums[i] <= 100
'''
def maxCoins(nums):
    n = len(nums)
    memo = {}
    
    def maxCoinsHelper(left, right):
        if left > right:
            return 0
        if (left, right) in memo:
            return memo[(left, right)]
        
        max_coins = 0
        for i in range(left, right + 1):
            coins = nums[i] * (nums[left - 1] if left > 0 else 1) * (nums[right + 1] if right < n - 1 else 1)
            max_coins = max(max_coins, coins + maxCoinsHelper(left, i - 1) + maxCoinsHelper(i + 1, right))
        
        memo[(left, right)] = max_coins
        return max_coins
    
    return maxCoinsHelper(0, n - 1)

# Test cases
import sys

if len(sys.argv) < 2:
    num_simulations = 1
else:
    if sys.argv[1] == "1":
        num_simulations = 1
    else:
        num_simulations = 1000000

for _ in range(num_simulations):
    nums = [3, 1, 5, 8]
    maxCoins(nums)

    nums = [1, 5]
    maxCoins(nums)


# nums1 = [3, 1, 5, 8]
# print(maxCoins(nums1))  # Output: 167

# nums2 = [1, 5]
# print(maxCoins(nums2))  # Output: 10
