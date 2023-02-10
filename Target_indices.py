class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums = sorted(nums)
        target_list = []
        for index in range(len(nums)):
            if nums[index] == target:
                target_list.append(index)
        return target_list
