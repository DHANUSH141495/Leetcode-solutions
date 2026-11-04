class Solution(object):
    def lengthOfLongestSubstring(self, s):
        dic={ }
        l=0
        max_=0
        
        for i in range(len(s)):
            cur = s[i]
            if cur in dic and dic[cur] >= l:
                l=dic[cur]+1
            dic[cur]=i
            max_= max(max_,i-l+1)
        return max_

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna