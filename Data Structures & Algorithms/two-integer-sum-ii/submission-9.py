class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # brute force = two for loops
        # for x in range(len(numbers)):
        #     for y in range(x+1, len(numbers)):
        #         if numbers[x] + numbers[y] == target:
        #             return [x+1, y+1]

        # we know the array is sorted in non-decreasing order
        # 1 pointer at the beginning, 1 at the end
        l, r = 0, len(numbers)-1

        while l < r:
            if numbers[l] + numbers[r] < target:
                l += 1
            if numbers[l] + numbers[r] > target:
                r -= 1
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]

        return None