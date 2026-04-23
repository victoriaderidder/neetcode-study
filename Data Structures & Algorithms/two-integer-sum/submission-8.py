class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        storage = {}
        for idx, x in enumerate(nums):
            diff = target - x
            print(diff, storage)
            if target - diff in storage:
                print(storage[target-diff])
                return [storage[target-diff], idx]
            storage[diff] = idx