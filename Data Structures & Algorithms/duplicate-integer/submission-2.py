class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen=set() #creating empty set to see if we have seen the elemtents before
        for num in nums: #loop through every elemnt in the list
            if num in seen: #condition to see if number is seen before
                return True #if seen return true means 4 is the new element and 4 is was seen last time
            else:
                seen.add(num) #else add the new value to seen list
        return False #outside loop return false so that no dups find
        #the main idea is to go through every number once in the list and add them seen list. The seen list will be matched with new number from the num list. This way we see every element once.