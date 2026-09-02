class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)-1
        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum == target:
                break
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return [left, right]