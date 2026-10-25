class Solution(object):
    def moveZeroes(self, nums):
       sc = 0 
       wr = 0
       while sc < len(nums):
            if nums[sc]!=0:
               nums[wr],nums[sc]=nums[sc],nums[wr]
               wr +=1
            sc +=1    
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna