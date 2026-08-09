class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # First Sol:
        # st = set()
        # n = len(nums)
        # nums.sort()

        # for i in range(n-2):
        #     j = i + 1
        #     k = n - 1
            
        #     while j < k:
        #         if nums[i] + nums[j] + nums[k] <= 0:
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 st.add((nums[i], nums[j], nums[k]))
        #             j += 1
                
        #         else:
        #             k -= 1
        
        # return [list(item) for item in st]

        # Second Sol
        res = []
        n = len(nums)
        nums.sort()

        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l, r = i + 1, n - 1
            while l < r:
                sm = nums[i] + nums[l] + nums[r]

                if sm > 0:
                    r -= 1
                elif sm < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        
        return res

