from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        tmp = []
        for i in nums:
            if i not in tmp:
                tmp.append(i)

        res = len(tmp)
        return res

    def removeDuplicates_inactive(self, nums: List[int]) -> int:
        tmp = []
        for i in nums:
            if i not in tmp:
                tmp.append(i)

        res = len(tmp)
        return res

    def romanToInt(self, s: str) -> int:
        romant_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        res = 0
        # Iterate through the string up to the second-to-last character
        for i in range(len(s) - 1):
            # Check if the current numeral is less than the next numeral
            if romant_dict[s[i]] < romant_dict[s[i + 1]]:
                res -= romant_dict[s[i]]  # Subtract if lesser
            else:
                res += romant_dict[s[i]]  # Add if not

        res += romant_dict[s[-1]]  # Always add the last numeral
        return res


if __name__ == "__main__":
    s = Solution()
    print("____RomanToInt____")
    print(f"Testcase 01 (should be 3): {s.romanToInt('III')}")
    print(f"Testcase 02 (should be 58): {s.romanToInt('LVIII')}")
    print(f"Testcase 03 (should be 1994): {s.romanToInt('MCMXCIV')}")
    print(f"Testcase 04 (should be 4): {s.romanToInt('IV')}")
    print("____WIP____")

    print(f"Testcase 04 (should be 4): {s.removeDuplicates([1, 1, 2])}")
