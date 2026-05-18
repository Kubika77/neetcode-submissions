from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_chars_dict = defaultdict(int)
        t_chars_dict = defaultdict(int)
        for char in s:
            if char in s:
                s_chars_dict[char] += 1
        for char in t:
            if char in t:
                t_chars_dict[char] += 1
        if s_chars_dict == t_chars_dict:
            return True
        return False
        