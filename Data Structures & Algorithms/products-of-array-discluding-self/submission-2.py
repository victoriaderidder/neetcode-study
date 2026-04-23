class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for x in range(len(nums)):
            index = 0
            product = 1
            while index < len(nums):
                if x != index:
                    product *= nums[index]
                index += 1
            res.append(product)
        return res
        