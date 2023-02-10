class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        smaller_list = [0]*len(nums)
        for index in range(len(nums)):
            for index2 in range(len(nums)):
                if nums[index] > nums[index2]:
                    smaller_list[index] += 1
                    
        return smaller_list
