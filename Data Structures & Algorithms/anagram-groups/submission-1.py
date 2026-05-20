class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = defaultdict(list)
        for string in strs:
            sorted_str = "".join(sorted(string))
            str_dict[sorted_str].append(string)
        return list(str_dict.values())