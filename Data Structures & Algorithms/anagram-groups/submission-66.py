class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        letter_a = ord("a")

        for word in strs:
            count = [0] * 26
            for char in word:
                index = ord(char) - letter_a
                count[index] += 1

            ans[tuple(count)].append(word)

        result = (list(ans.values()))

        return result