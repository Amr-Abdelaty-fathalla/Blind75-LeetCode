class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # First Solution: hash
        ind_dict = {}
        ind_lst = []

        if len(nums) == 0:
            return []

        for idx in range(len(nums)):

            if (target - nums[idx]) in ind_dict:
                ind_lst.append(ind_dict.get(target-nums[idx]))
                ind_lst.append(idx)
        
            ind_dict[nums[idx]] = idx

        return ind_lst


