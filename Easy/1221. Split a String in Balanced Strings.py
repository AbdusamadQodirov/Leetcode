# Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

# Given a balanced string s, split it into some number of substrings such that:

#     Each substring is balanced.

# Return the maximum number of balanced strings you can obtain.

 

# Example 1:

# Input: s = "RLRRLLRLRL"
# Output: 4
# Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.

# Example 2:

# Input: s = "RLRRRLLRLL"
# Output: 2
# Explanation: s can be split into "RL", "RRRLLRLL", each substring contains same number of 'L' and 'R'.
# Note that s cannot be split into "RL", "RR", "RL", "LR", "LL", because the 2nd and 5th substrings are not balanced.

# Example 3:

# Input: s = "LLLLRRRR"
# Output: 1
# Explanation: s can be split into "LLLLRRRR".

# Solution
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        sal = []
        k, j = 0, 0
        res = 0
        res1 = 0
        for i in s:
            if i == 'R':
                k += 1
            if i == "L":
                j += 1
            if k == j:
                sal.append(s[res1:res])
                res1 = res
            res += 1

        return len(sal)