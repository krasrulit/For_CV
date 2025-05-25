"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        x = 0
        result = []

        while x != len(nums) - 2:
            if x > 0 and nums[x] == nums[x - 1]:
                x += 1
                continue
                
            left = x + 1
            right = len(nums) - 1

            while left<right:
                total = nums[x] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[x], nums[left], nums[right]])

                    while left<right and nums[left] == nums[left + 1]:
                        left += 1
                    while left<right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif total < 0:
                    left += 1
                elif total > 0:
                    right -= 1

            x += 1
            
        return result
