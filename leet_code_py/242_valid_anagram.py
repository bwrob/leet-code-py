from collections import Counter


class Solution:
    def isAnagram_decrease_increase_no_dict(self, s: str, t: str) -> bool:
        position_shift = ord("a")
        memory_dict = [0] * 26
        for l in s:
            memory_dict[ord(l) - position_shift] += 1
        for l in t:
            memory_dict[ord(l) - position_shift] += -1
        return all(letter_count == 0 for letter_count in memory_dict)

    def isAnagram_decrease_increase(self, s: str, t: str) -> bool:
        memory_dict = {}

        def __process_word(word: str, appender: int) -> None:
            for letter in word:
                if letter in memory_dict:
                    memory_dict[letter] = memory_dict[letter] + appender
                else:
                    memory_dict[letter] = appender

        __process_word(s, 1)
        __process_word(t, -1)
        return all(letter_count == 0 for letter_count in memory_dict.values())

    def isAnagram_counter(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
