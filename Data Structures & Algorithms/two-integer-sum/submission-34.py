class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previous_nums = defaultdict() #maps val to index

        for index, number in enumerate(nums):
            diff = target - number
            if diff in previous_nums: #hash map therefore constant time complexity
                return [previous_nums[diff], index]
            
            previous_nums[number] = index
        return []