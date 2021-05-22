class Solution:
    def addBinary(self, a: str, b: str) -> str:
        l1, l2 = len(a), len(b)
        cursor, inc = 1, 0
        val = []
        while cursor <= l1 or cursor <= l2:
            n1 = int(a[-cursor]) if cursor <= l1 else 0
            n2 = int(b[-cursor]) if cursor <= l2 else 0
            n = n1 + n2 + inc
            if n > 1:
                n, inc = n - 2, 1
            else:
                inc = 0
            val.insert(0, str(n))
            cursor += 1
        if inc:
            val.insert(0, str(inc))
        return ''.join(val)
