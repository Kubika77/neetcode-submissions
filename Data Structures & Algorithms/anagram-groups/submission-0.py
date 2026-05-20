class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strings_dict = defaultdict(list)
        for string in strs:
            string_array_key = [0] * 26
            for char in string:
                char_idx = (ord(char) - ord("a"))
                string_array_key[char_idx] += 1
            string_key = tuple(string_array_key)
            strings_dict[string_key].append(string)
        return list(strings_dict.values())