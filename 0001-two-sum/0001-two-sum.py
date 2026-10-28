class Solution(object):
    def twoSum(self, nums, target):
        seen ={}
        for index,n in enumerate(nums):
            need =target -n
            if need in seen:
               return [seen[need], index]
            else:
                seen[n]=index

        # Current implementation uses a brute-force double loop.
        # Time Complexity: O(n^2) because for each i we scan all j > i.
        # Space Complexity: O(1) (excluding output list).
        # This works for the problem constraints but is not optimal.
        # A hash map can reduce time to O(n) with O(n) extra space.
        # Also, the initial i and j assignments are unnecessary.
        # i = 0
        # j = i+1
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if  nums[i] + nums[j]==target:
        #             # Found the required pair; return their indices.
        #             return [i,j]
        #         else:
        #              # The else block manually increments j, which is redundant
        #              # because the for-loop already increments j automatically.
        #              # This line can be removed.
        #              j+=1
       

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna