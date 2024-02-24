class Solution:
    shift = ord("a")

    def to_hash(self, word: str) -> tuple[int, ...]:
        ls = [0] * 26
        for lett in word:
            ls[ord(lett) - self.shift] += 1
        return tuple(ls)

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        counter_dict = {}
        for ls in strs:
            count = self.to_hash(ls)
            if count in counter_dict:
                counter_dict[count].append(ls)
            else:
                counter_dict[count] = [ls]

        return list(counter_dict.values())
