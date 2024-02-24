class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        memory_set = set()
        for item in nums:
            if item in memory_set:
                return True
            memory_set.add(item)
        return False
