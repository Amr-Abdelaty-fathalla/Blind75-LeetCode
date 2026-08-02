class Solution:
    def is_alphanumeric(self, x):
        return ((ord('A') <= x <= ord('Z')) or 
                (ord('a') <= x <= ord('z')) or 
                (ord('0') <= x <= ord('9')))

    def isPalindrome(self, s: str) -> bool:
        ptr_r, ptr_l = 0, len(s) - 1

        while ptr_r <= ptr_l:
            
            if not self.is_alphanumeric(ord(s[ptr_r])):
                ptr_r += 1
                continue          

            if not self.is_alphanumeric(ord(s[ptr_l])):
                ptr_l -= 1
                continue
            

            if s[ptr_r].lower() != s[ptr_l].lower():
                return False
            
            ptr_r += 1
            ptr_l -= 1
            
        return True

        
        