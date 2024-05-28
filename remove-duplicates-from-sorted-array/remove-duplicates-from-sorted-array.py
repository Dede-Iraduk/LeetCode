class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1  # Initialize a pointer j starting at index 1
        for i in range(1, len(nums)):  # Iterate from the second element to the end of the array
            if nums[i] != nums[i - 1]:  # If the current element is different from the previous element
                nums[j] = nums[i]  # Place the current element at the j-th position
                j += 1  # Move the j pointer to the next position
        return j  # Return the number of unique elements
