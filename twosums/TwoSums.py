from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)

        # Build the hash table
        for i in range(n):
            numMap[nums[i]] = i

        # Find the complement
        for i in range(n):
            complement = target - nums[i]
            if complement in numMap and numMap[complement] != i:
                return [i, numMap[complement]]

        return []  # No solution found

    def main(self):
        solution = Solution()

        #   test_case01 = solution.twoSum([2, 7, 11, 15], 9)
        #   test_case02 = solution.twoSum([3,2,4], 6)
        #   test_case03 = solution.twoSum([3,3], 6)
        test_case04 = solution.twoSum([3, 5, 4], 7)
        test_case05 = solution.twoSum([3, 0, 0, 0, 0, 0, 0, 4], 7)

        print(test_case05)


if __name__ == "__main__":
    Solution().main()
