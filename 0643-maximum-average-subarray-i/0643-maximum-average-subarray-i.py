class Solution(object):
    def findMaxAverage(self, nums, k):
        cur_sum =0
        for i in range(k):
            cur_sum += nums[i]
        max_sum=cur_sum
        for i in range(k,len(nums)):
            cur_sum-=nums[i-k]
            cur_sum+=nums[i]
            if cur_sum>max_sum:
                  max_sum=cur_sum

        return float(max_sum)/k    

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna