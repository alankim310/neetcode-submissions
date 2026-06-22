class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        result = 0

        for i, n in enumerate(nums):
            if n == val:
                pass
            elif n != val:
                nums[k] = nums[i]
                k += 1
            print(i,n)
            pass

        return k