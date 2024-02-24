from collections import Counter
from functools import reduce
from operator import mul


class Solution:
    def productExceptSelf_naive(self, nums: list[int]) -> list[int]:
        count = Counter(nums)

        if count[0] > 1:
            return [0] * len(nums)

        if count[0] == 1:
            non_zero = [item for item in nums if item != 0]
        else:
            non_zero = nums

        product_all = reduce(mul, non_zero, 1)

        if count[0] == 1:
            result = [0] * len(nums)
            result[nums.index(0)] = product_all
            return result

        return [int(product_all / item) for item in nums]
