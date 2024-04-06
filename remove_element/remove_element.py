from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Initialize a pointer for the position of the next non-val element
        position = 0
        f = nums

        # Iterate through the nums array
        for i in range(len(nums)):
            # If the current element is not val
            if nums[i] != val:
                # Move it to the 'position' index
                nums[position] = nums[i]
                # Increment the position pointer
                position += 1

        # 'position' now holds the count of elements not equal to 'val'
        # and nums is modified in-place to hold these elements at the start
        return position

    def remove_element_old(self, nums: List[int], val: int) -> int:
        res = 0
        for i in nums:
            if i != val:
                res = i
        return res


# Example usage:
s = Solution()
# print(s.removeElement([3, 2, 2, 3], 3))  # Expected output: 2
print(s.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))  # Expected output: 2
