# Approach 1: Use a set
# Approach 2: Iterate and check if exists in a separate list
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_set = set(nums)
        unique_list = list(unique_set)
        unique_list_len = len(unique_list)
        # print(unique_list)
        return len(unique_set)