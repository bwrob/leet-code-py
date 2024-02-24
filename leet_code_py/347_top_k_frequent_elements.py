class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        memory_dict = {}
        for i in nums:
            if i in memory_dict:
                memory_dict[i] += 1
            else:
                memory_dict[i] = 1

        max_frec = max(memory_dict.values())
        frec_dict = {i: [] for i in range(max_frec + 1)}

        for num, frec in memory_dict.items():
            frec_dict[frec].append(num)
        result = []
        for frec in reversed(range(max_frec + 1)):
            result += frec_dict[frec]
            if len(result) > k:
                break
        return result[:k]
