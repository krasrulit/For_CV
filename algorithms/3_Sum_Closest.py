"""
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        result = None
        nums.sort()
        index = 0

        while index != len(nums) - 2:
            if index > 0 and nums[index] == nums[index - 1]: 
                index += 1
                continue
            
            left = index + 1
            right = len(nums) - 1

            while left < right:
                candidate = nums[index] + nums[left] + nums[right]

                if (result is None) or (abs(target - candidate) < abs(target - result)):
                    result = candidate

                elif candidate == target:
                    return result

                elif candidate < target:
                    left += 1
                
                else:
                    right -= 1

            index += 1

        return result
