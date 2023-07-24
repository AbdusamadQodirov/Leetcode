# Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

# For example:

# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 
# ...

 

# Example 1:

# Input: columnNumber = 1
# Output: "A"

# Example 2:

# Input: columnNumber = 28
# Output: "AB"

# Example 3:

# Input: columnNumber = 701
# Output: "ZY"

# Solution

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        output = "" # create new empty string
        while columnNumber > 0:
            res = (columnNumber - 1) % 26 
            columnNumber = (columnNumber - 1) // 26
            output += chr(int(res) + ord('A'))
        
        output = output[::-1]
        return output