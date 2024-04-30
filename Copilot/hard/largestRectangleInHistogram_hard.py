'''
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.
Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:
Input: heights = [2,4]
Output: 4
 

Constraints:

1 <= heights.length <= 105
0 <= heights[i] <= 104
'''
def largestRectangleArea(heights):
    stack = []
    max_area = 0
    i = 0
    while i < len(heights):
        if not stack or heights[i] >= heights[stack[-1]]:
            stack.append(i)
            i += 1
        else:
            top = stack.pop()
            area = heights[top] * (i if not stack else i - stack[-1] - 1)
            max_area = max(max_area, area)
    while stack:
        top = stack.pop()
        area = heights[top] * (i if not stack else i - stack[-1] - 1)
        max_area = max(max_area, area)
    return max_area

# Test the function
import sys

if len(sys.argv) < 2:
    num_simulations = 1
else:
    if sys.argv[1] == "1":
        num_simulations = 1
    else:
        num_simulations = 10000000

for _ in range(num_simulations):
    heights = [2, 1, 5, 6, 2, 3]
    largestRectangleArea(heights)

    heights = [2, 4]
    largestRectangleArea(heights)


# heights = [2, 1, 5, 6, 2, 3]
# print(largestRectangleArea(heights))  # Output: 10

# heights = [2, 4]
# print(largestRectangleArea(heights))  # Output: 4