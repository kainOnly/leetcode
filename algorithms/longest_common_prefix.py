from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        x, y = 0, 0
        val, char = '', ''
        while True:
            if y > len(strs) - 1:
                val += char
                char = ''
                y = 0
                x += 1
            if x > len(strs[y]) - 1:
                break
            if char == '':
                char = strs[y][x]
            else:
                if char != strs[y][x]:
                    break
            y += 1

        return val
