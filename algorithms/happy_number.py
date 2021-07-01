class Solution:
    def isHappy(self, n: int) -> bool:
        def getNext(num: int):
            m = 0
            while num > 0:
                num, x = divmod(num, 10)
                m += x ** 2
            return m

        slow = n
        fast = getNext(n)
        while fast != 1 and fast != slow:
            slow = getNext(slow)
            fast = getNext(getNext(fast))

        return fast == 1
