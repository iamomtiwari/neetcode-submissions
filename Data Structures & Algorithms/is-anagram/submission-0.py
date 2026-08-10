#Brute force plan:
#If len(s) != len(t), return False immediately (different lengths can't be anagrams).
#For each character in s, count how many times it appears in s, and count how many times that same character appears in t. If those two counts ever differ, return False.
#If you get through all characters without a mismatch, return True
#use python .count() method
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):return False
        for i in s:
            if s.count(i)!=t.count(i):
                return False
        return True