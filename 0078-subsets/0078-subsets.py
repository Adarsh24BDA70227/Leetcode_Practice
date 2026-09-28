class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(start, path):
            if start >= len(nums):
                result.append(path[:])
                return
            path.append(nums[start])
            backtrack(start + 1, path)
            path.pop()
            backtrack(start + 1, path)
        backtrack(0, [])
        return result