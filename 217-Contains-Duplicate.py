class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # First Solution: Sort Array
        # if len(nums) == 0:
        #     return False

        # nums.sort()
        # for i in range(1,len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return True
        
        # return False



        # Second Solution: Set
        # uni_nums = set()

        # if len(nums) == 0:
        #     return False

        # for i in nums:
        #     if i in uni_nums:
        #         return True
            
        #     uni_nums.add(i)
        
        # return False



        # Third Solution: Array Length
        uni_nums_set = set(nums)

        if len(nums) == 0:
            return False
        
        if len(uni_nums_set) == len(nums):
            return False
        
        return True



        