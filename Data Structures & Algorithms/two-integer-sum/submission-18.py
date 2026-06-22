class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []

        for i in range(len(nums)):
            print(i)
            num = nums[i]
            diff = target - num
            print(f"this is num {num}")
            print(f"this is diff {diff}")
            print(f"this is type diff {type(diff)}")

            if diff in nums[i+1: ]:
                diff_index = nums.index(diff, i + 1)
                result.append(i)
                result.append(diff_index)

        return result