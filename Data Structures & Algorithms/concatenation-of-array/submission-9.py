class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nested_ans = []
        nested_ans.append(nums)
        nested_ans.append(nums)

        ans = [item for sublist in nested_ans for item in sublist]

        
        return ans
        