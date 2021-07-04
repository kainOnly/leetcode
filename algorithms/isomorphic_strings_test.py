import unittest
from .isomorphic_strings import Solution


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.isIsomorphic("egg", "add"), True)

    def test_example2(self):
        self.assertEqual(self.sol.isIsomorphic("foo", "bar"), False)

    def test_example3(self):
        self.assertEqual(self.sol.isIsomorphic("paper", "title"), True)
