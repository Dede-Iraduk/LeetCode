class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # use 2 iterators through the array of numbers
        # i which iterates through the array and j which keeps track of the encountered 0s
        # if element not 0,0, append it to th end of the array
        
        j = 0
        for i in range(len(nums)):
            if nums[i]!= 0:
                nums[j], nums[i] = nums[i], nums[j]
                j +=1
        