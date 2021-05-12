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
                if len(stack) > 0 and stack[-1] != find[char]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(char)
        return True
