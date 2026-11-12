class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        seen = set()
  

        for i in range (len(nums)):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
            if len(seen)>  k:
               seen.remove(nums[i-k])
        return False
        
            
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna