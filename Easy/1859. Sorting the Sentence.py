# A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each word consists of lowercase and uppercase English letters.

# A sentence can be shuffled by appending the 1-indexed word position to each word then rearranging the words in the sentence.

#     For example, the sentence "This is a sentence" can be shuffled as "sentence4 a3 is2 This1" or "is2 sentence4 This1 a3".

# Given a shuffled sentence s containing no more than 9 words, reconstruct and return the original sentence.

 

# Example 1:

# Input: s = "is2 sentence4 This1 a3"
# Output: "This is a sentence"
# Explanation: Sort the words in s to their original positions "This1 is2 a3 sentence4", then remove the numbers.

# Example 2:

# Input: s = "Myself2 Me1 I4 and3"
# Output: "Me Myself and I"
# Explanation: Sort the words in s to their original positions "Me1 Myself2 and3 I4", then remove the numbers.

                                    # Solution


class Solution:
    def sortSentence(self, s: str) -> str:
        s1 = s.split(" ") # split funksiyasi list yaratadi har " " belgi orasida
        output = ["" for i in range(len(s1))] # s1 list uzunligiga mos bo'sh qiymatlarni qabul qiladi
        for i in range(len(s1)):
            output[int(s1[i][-1]) - 1] = s1[i][:-1] # bu har bir qiymatni oxirgi indeksdagi qiymatdan 1 ni ayirib output degan listning shu indexiga oxirgi sonni olmasdan joylab ketadi
    # ya'ni har bir qiymatni oxirgi soniga qaridi va undan birni ayirib listga shu qiymatni joylab ketadi
        
        return " ".join(output) # va listni bitta so'zga aylantirib qaytarib yuboradi