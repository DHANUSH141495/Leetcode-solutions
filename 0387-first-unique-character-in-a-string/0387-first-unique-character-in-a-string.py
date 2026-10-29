class Solution(object):
    def firstUniqChar(self, s):
        count={}
        for i in s:
            count[i] = count.get(i,0)+1
        for index,i in enumerate(s):
            if count[i] ==1:
               return index
        return -1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna