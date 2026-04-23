class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        storage = []
        for x in nums:
            if x in storage:
                return True
            storage.append(x)
        return False
            
         