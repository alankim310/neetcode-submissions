class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        first_str = strs[0]
        if first_str == "":
            return ans

        for i in range(len(first_str)):
            map_list = list((map(lambda word: word.find(ans + first_str[i]), strs)))
            if all(x == 0 for x in map_list):
                ans += first_str[i]
            else:
                return ans

        return ans