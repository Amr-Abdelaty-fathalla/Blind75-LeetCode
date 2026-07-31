class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # First sol time:O(n), space: O(n)
        # prefix_pro = []
        # suffix_pro = []
        # ans= []

        # l = 1
        # for i in range(len(nums)):
        #     prefix_pro.append(l)
        #     l *= nums[i]
        
        # r = 1
        # for i in range(len(nums) - 1, -1, -1):
        #     suffix_pro.append(r)
        #     r *= nums[i]

        # for j in range(len(prefix_pro)):
        #     ans.append(prefix_pro[j] * suffix_pro[(len(suffix_pro)-1) - j])

        # return ans 

        # Second Sol time: O(n), space: O(1)
        ans = [1] * len(nums)

        l = 1
        for i in range(len(nums)):
            ans[i] = l
            l *= nums[i]

        r = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= r
            r *= nums[i]
        
        return ans
        