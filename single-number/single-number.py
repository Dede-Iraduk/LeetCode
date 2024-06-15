class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # store the elements in a dictionary
        # from the elements in the dictionary, check from one where freq !=2

        # store the elements in a dictionary
        newnums = {}
        for num in nums:
            if num in newnums:
                newnums[num] += 1
            else:
                newnums[num] = 1
                
        # find the element with frequency 1
        for key, value in newnums.items():
            if value == 1:
                return key

        
            
            