
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)  # Length of the input array
        n1 = 0  # Counter for number of 1s encountered so far
        n0 = 0  # Counter for number of 0s encountered so far
        maxLen = 0  # Variable to keep track of the maximum length of the subarray found
        mp = {}  # Dictionary to store the first occurrence of a particular difference between n1 and n0
        mp[0] = -1  # Initialize with a base case for handling subarrays starting from index 0

        for i in range(n):
            n1 += nums[i]  # Increment the 1s counter if the current element is 1
            n0 = (i + 1) - n1  # Calculate the number of 0s encountered so far
            diff = n1 - n0  # Calculate the difference between the count of 1s and 0s

            if diff in mp:  # Check if this difference has been seen before
                # If we have seen this difference before, it means the subarray from mp[diff] + 1 to i has equal 0s and 1s
                maxLen = max(maxLen, i - mp[diff])  # Update the maximum length of the subarray
            else:
                mp[diff] = i  # Store the current index as the first occurrence of this difference

        return maxLen  # Return the maximum length found

    




    
        