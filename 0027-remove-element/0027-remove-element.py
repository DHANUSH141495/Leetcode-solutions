class Solution(object):
    def removeElement(self, nums, val):
        k=0
        right=0
        while right<len(nums):
            if nums[right]!= val:
                nums[k]=nums[right]
                k+=1
            right+=1
        return k        
            
       
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna