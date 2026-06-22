class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previous_nums = defaultdict() #maps val to index

        for index, number in enumerate(nums):
            diff = target - number
            print(f"this is index {index}\n this is number {number}\n")

            if diff in previous_nums: #hash map therefore constant time complexity
                return [previous_nums[diff], index]
            
            previous_nums[number] = index
            print(f"this is our previous_nums {previous_nums}")
        return []