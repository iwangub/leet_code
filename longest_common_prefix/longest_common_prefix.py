from typing import List


class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        tmp_common_prefix = ""
        end_of_word = False

        for str in strs:
            for str2 in strs:
                if end_of_word:
                    tmp_common_prefix = ""
                if str == str2:
                    continue
                str_len = min(len(str), len(str2), )
                for i in range(str_len):
                    if str[i] == str2[i]:
                        tmp_common_prefix += str[i]
                        if len(tmp_common_prefix) > len(res):
                            res = tmp_common_prefix
                    if i == str_len - 1:
                        end_of_word = True
        return res

    def test(self, strs):
        for str in strs:
            if str == "2":
                print("same")
        return


s = Solution()
print(f'WIP 1: {s.test(["string", "2"])}')

print(f'Test 1: {s.longestCommonPrefix(["flower", "flowerxxxxxxx", "flight", "flowerx"])}')

print(f'Test 2: {s.longestCommonPrefix(["dog", "racecar", "car"])}')

print(f'Test 3: {s.longestCommonPrefix(["flower", "flow", "flight"])}')
