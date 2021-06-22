class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        find = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []
        for char in s:
            if char in find:
                if not stack or stack[-1] != find[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        return not stack
