class Solution:
    def maxArea(self, height: List[int]) -> int:
        # steps
        # ptr_r, ptr_l, max_area = 0, len(nums) - 1, 0
        # edge case if len (nums) == 0,1 return area 0
        # loop until ptr_r == ptr_l, while ptr_r < ptr_l
        # minus indicies of ptr_l from ptr_r 
        # multiply result of minus indicies * the min from (height[ptr_r], height[ptr_l])
        # get max between (old max_area, result of multiply)
        # assign it in max_area
        # check if height[ptr_r] smaller than or equal height[ptr_l]: add ptr_r += 1
        # else: sub ptr_l -= 1
        # return max_area

        ptr_r, ptr_l, max_area = 0, len(height) - 1, 0

        if (len(height) == 0) or (len(height) == 1):
            return max_area
        
        while ptr_r < ptr_l:
            min_height = min((height[ptr_r], height[ptr_l]))
            max_area = max(max_area, ((ptr_l - ptr_r) * min_height))

            if height[ptr_r] <= height[ptr_l]:
                ptr_r += 1
            
            else:
                ptr_l -= 1
        
        return max_area
        