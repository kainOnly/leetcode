class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'
        if n == 1:
            return s
        while n != 1:
            val = ''
            cursor1, cursor2 = 1, 0
            while cursor1 < len(s):
                if s[cursor1] != s[cursor2]:
                    val += str(cursor1 - cursor2) + s[cursor2]
                    cursor2 = cursor1
                cursor1 += 1
            val += str(len(s) - cursor2) + s[cursor2]
            s = val
            n -= 1
        return s
