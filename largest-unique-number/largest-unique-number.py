class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        # Create a hashtable to store the occurrences of each number
        num_counts = {}
        for num in nums:
            num_counts[num] = num_counts.get(num, 0) + 1

        # Initialize the largest unique number to -1
        largest_unique = -1

        # Iterate through the hashtable to find the largest unique number
        for num, count in num_counts.items():
            if count == 1 and num > largest_unique:
                largest_unique = num

        return largest_unique


        
        