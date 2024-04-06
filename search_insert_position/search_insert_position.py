from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        if target <= nums[0]:
            return 0
        for i in range(len(nums) - 1):  # Stop before the last element
            if target > nums[i] and target <= nums[i + 1]:
                return i + 1
        return len(nums)  # If target is greater than all elements in nums


s = Solution()

print(f"Example01: {s.searchInsert([1, 3, 5, 6], 5)}")
print(f"Example02: {s.searchInsert([1, 3, 5, 6], 2)}")
print(f"Example03: {s.searchInsert([1, 3, 5, 6], 7)}")
