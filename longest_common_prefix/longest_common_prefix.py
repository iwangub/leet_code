from typing import List


class Solution:

    def longest_unique_prefix(self, strs: List[str]) -> str:
        res = ""
        tmp_common_prefix = ""

        for str in strs:
            for str2 in strs:
                if str == str2:
                    continue
                str_len = min(len(str), len(str2), )
                for i in range(str_len):
                    if str[i] == str2[i]:
                        tmp_common_prefix += str[i]
                        if len(tmp_common_prefix) > len(res):
                            res = tmp_common_prefix
                    if i == str_len - 1:
                        tmp_common_prefix = ""

        return res

    def longest_common_prefix(self, strs: List[str]) -> str:
        res = ''
        longest_prefix = self.longest_unique_prefix(strs)
        common_prefix = ''

        for str in strs:
            if str == longest_prefix:
                continue
            str_len = min(len(str), len(longest_prefix))
            for i in range(str_len):
                if str[i] == longest_prefix[i]:
                    common_prefix += str[i]
                if len(common_prefix) > len(res):
                    res = common_prefix
                if i == str_len - 1:
                    common_prefix = ""
        return res

    def test(self, strs):
        for str in strs:
            if str == "2":
                print("same")
        return


s = Solution()
print(f'WIP 1: {s.test(["string", "2"])}')

print(f'Test longest_UNIQUE_prefix 1: {s.longest_unique_prefix(["flower", "flow", "flight"])}')

# print(f'Test longest_UNIQUE_prefix 2: {s.longest_unique_prefix(["dog", "racecar", "car"])}')

# print(f'Test longest_UNIQUE_prefix 3: {s.longest_unique_prefix(["flower", "flow", "flight"])}')

print(f'Test longest_COMMON_prefix 1: {s.longest_common_prefix(["flower", "flow", "flight"])}')

print(f'Test longest_COMMON_prefix 2: {s.longest_common_prefix(["dog", "racecar", "car"])}')

# print(f'Test longest_COMMON_prefix 3: {s.longest_common_prefix(["flower", "flow", "flight"])}')
