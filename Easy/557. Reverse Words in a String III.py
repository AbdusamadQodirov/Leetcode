# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

# Example 1:

# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"

# Example 2:

# Input: s = "God Ding"
# Output: "doG gniD"

# Solution


class Solution:
    def reverseWords(self, s: str) -> str:
        s1 = s.split(" ") # bu kod probelgacha bo'lgan qiymatni listga joylab boradi
        for i in range(len(s1)):
            s1[i] = s1[i][::-1] # bu har bir qiymatni olib uni teskari aylantiradi
        return " ".join(s1) # bu kod listni qo'shib yuboradi

    