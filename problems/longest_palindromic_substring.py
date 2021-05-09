# TODO:待优化
class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindrome = s[0]
        length, cursor = len(s), 0
        if length < 2:
            return palindrome
        while cursor < length:
            expand1, expand2 = 1, 1
            # odd
            while True:
                rindex = cursor - expand1
                lindex = cursor + expand1
                if rindex < 0 or lindex > length - 1:
                    break
                right, left = s[rindex], s[lindex]
                if right == left:
                    sec = s[rindex:lindex + 1]
                    if len(sec) > len(palindrome):
                        palindrome = sec
                    expand1 += 1
                else:
                    break
            # even
            while True:
                rindex = cursor + 1 - expand2
                lindex = cursor + expand2
                if rindex < 0 or lindex > length - 1:
                    break
                right, left = s[rindex], s[lindex]
                if right == left:
                    sec = s[rindex:lindex + 1]
                    if len(sec) > len(palindrome):
                        palindrome = sec
                    expand2 += 1
                else:
                    break
            cursor += 1
        return palindrome
