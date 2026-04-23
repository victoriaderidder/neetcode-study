class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in range(len(nums)):
            for y in range(len(nums) - 1):
                print(x, y+1)
                if nums[x] + nums[y+1] == target and x != y+1:
                    return [x, y+1]