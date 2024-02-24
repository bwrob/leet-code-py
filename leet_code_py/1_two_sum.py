class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        memory_dict = {}
        for idx, item in enumerate(nums):
            if item in memory_dict:
                return [memory_dict[item], idx]
            memory_dict[target - item] = idx
        print(memory_dict)
        return []
