'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
'''
def findMedianSortedArrays(nums1, nums2):
    # Merge the two sorted arrays
    merged = sorted(nums1 + nums2)
    
    # Calculate the length of the merged array
    length = len(merged)
    
    # Check if the length is even or odd
    if length % 2 == 0:
        # If even, return the average of the middle two elements
        return (merged[length // 2 - 1] + merged[length // 2]) / 2
    else:
        # If odd, return the middle element
        return merged[length // 2]
    
# Test cases

import sys

if len(sys.argv) < 2:
    num_simulations = 1
else:
    if sys.argv[1] == "1":
        num_simulations = 1
    else:
        num_simulations = 10000000

for _ in range(num_simulations):
    findMedianSortedArrays([1,3], [2])
    findMedianSortedArrays([1,2], [3,4])


# print(findMedianSortedArrays([1,3], [2]))     # Output: 2.00000
# print(findMedianSortedArrays([1,2], [3,4]))   # Output: 2.50000