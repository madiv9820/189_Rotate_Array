from Solution import Solution
import unittest
from timeout_decorator import timeout

class UnitTest(unittest.TestCase):
    def setUp(self) -> None:
        self.__testCases = {
            1: {'nums': [1,2,3,4,5,6,7], 'k': 3, 'output': [5,6,7,1,2,3,4]},
            2: {'nums': [-1,-100,3,99], 'k': 2, 'output': [3,99,-1,-100]}
        }

        self.__obj = Solution()

        return super().setUp()

    @timeout(0.5)
    def test_Case1(self):
        nums, k, output = self.__testCases[1].values()
        self.__obj.rotate(nums, k)
        self.assertEqual(nums, output)

    @timeout(0.5)
    def test_Case2(self):
        nums, k, output = self.__testCases[2].values()
        self.__obj.rotate(nums, k)
        self.assertEqual(nums, output)

if __name__ == '__main__': unittest.main()