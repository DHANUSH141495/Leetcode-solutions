class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums)<= 2:
            return len(nums)
        k = 2
        right =2
        while right <len(nums):
            if nums[right]!= nums[k-2]:
                nums[k]=nums[right]
                k+=1
            right+=1
        return k
     
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna