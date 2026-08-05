# 📖 Problem

# Given an array of distinct integers candidates and an integer target, return every unique combination where the chosen numbers add up to target.

# You may use the same number unlimited times.

# 💻 Example
# Input:
# candidates = [2,3,6,7]
# target = 7

# Output:
# [
#  [2,2,3],
#  [7]
# ]
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        combination = []

        def backtrack(start, current_sum):
            if current_sum == target:
                result.append(combination[:])
                return

            if current_sum > target:
                return

            for i in range(start, len(candidates)):
                combination.append(candidates[i])
                backtrack(i, current_sum + candidates[i])
                combination.pop()

        backtrack(0, 0)
        return result