# Leetcode
## Uzbek
Bu repositoryda men https://leetcode.com/ da ishlagan misollarim yechimini saqlab boraman.
Bu repositoryda men har bir bir misol uchun alohida faylda javoblarni yukladim savollari bilan birgalikda.
Birinchi savolni undan keyin yechimni ko'rishni maslahat beraman
Leetcode saytida amazon, google va boshqa katta kompaniyalarga kirishga tayyorgarlik savollari ham mavjud.
Men leetcode yechilgan masalalarni saralash uchun 3 ta fayl yaratdim ya'ni oson, o'rtacha va qiyin.
## English
In this repository, I keep the solutions of the examples I worked on in https://leetcode.com/ site
In this repository, I have uploaded the answers in a separate file for each example along with the questions.
I recommend to see the first question and then the solution
Leetcode also has entrance preparation questions for amazon, google and other big companies.
I have created 3 files to sort leetcode solved problems ie easy, medium and hard.
## For example:
### Question.      Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

### Solution.
```
class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
    'I' : 1,
    'V' : 5,
    'X' : 10,
    'L' : 50,
    'C' : 100,
    'D' : 500,
    'M' : 1000
}
        k = 0
        for i in range(1, len(s)):
            if values[s[i - 1]] >= values[s[i]]:
                k += values[s[i - 1]]
            else:
                k -= values[s[i - 1]]
        k += values[s[-1]]
        return k
```
