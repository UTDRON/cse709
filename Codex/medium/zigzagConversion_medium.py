'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
 

Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
'''
def convert(s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
        return s

    # Initialize rows
    rows = [''] * numRows

    # Initialize current row and direction
    current_row = 0
    direction = 1

    # Iterate through each character in the string
    for char in s:
        # Assign the character to the current row
        rows[current_row] += char

        # Update current row and direction
        current_row += direction
        if current_row == 0 or current_row == numRows - 1:
            direction *= -1

    # Concatenate rows to form the zigzag pattern
    return ''.join(rows)

# Example usage:
import sys

if len(sys.argv) < 2:
    num_simulations = 1
else:
    if sys.argv[1] == "1":
        num_simulations = 1
    else:
        num_simulations = 10000000

for _ in range(num_simulations):
    s1 = "PAYPALISHIRING"
    numRows1 = 3
    convert(s1, numRows1)

    s2 = "PAYPALISHIRING"
    numRows2 = 4
    convert(s2, numRows2)

    s3 = "A"
    numRows3 = 1
    convert(s3, numRows3)


# s1 = "PAYPALISHIRING"
# numRows1 = 3
# print(convert(s1, numRows1))  # Output: "PAHNAPLSIIGYIR"

# s2 = "PAYPALISHIRING"
# numRows2 = 4
# print(convert(s2, numRows2))  # Output: "PINALSIGYAHRPI"

# s3 = "A"
# numRows3 = 1
# print(convert(s3, numRows3))  # Output: "A"
