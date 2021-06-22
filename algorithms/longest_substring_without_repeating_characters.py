class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 1
        m = 0
        length = len(s)
        while right < length:
            index = s[left:right].find(s[right])
            if index != -1:
                n = right - left
                if m < n:
                    m = n
                left += index + 1
            else:
                if right == length - 1:
                    n = length - left
                    if m < n:
                        m = n
            right += 1
        if m == 0:
            m = length

        return m
