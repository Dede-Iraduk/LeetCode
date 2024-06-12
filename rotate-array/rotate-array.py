class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # ensuring k doesn't go out of bound
        k = k % n
        # nums[:k]: get the last k elements of the array != nums[:k]: get elements from the first one to the k element and concatenating the two slices
        nums[:] = nums[-k:] + nums[:-k]
        