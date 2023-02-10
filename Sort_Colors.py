class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for index in range(len(nums)):
            for index1 in range(len(nums)):
                if nums[index] <= nums[index1]:
                    temp = nums[index]
                    nums[index] = nums[index1]
                    nums[index1] = temp
