class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sol Time: 0(n), space: 0(n)
        st = set()
        r = mx = 0

        for l in range(len(s)):
            while r < len(s) and s[r] not in st:
                st.add(s[r])
                r += 1
                mx = max(mx, r-l)
        
            st.remove(s[l])
        
        return mx



