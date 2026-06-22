class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []

        for i in range(len(nums)):
            num = nums[i]
            diff = target - num

            if diff in nums[i+1: ]:
                diff_index = nums.index(diff, i + 1)
                result.append(i)
                result.append(diff_index)

        return result