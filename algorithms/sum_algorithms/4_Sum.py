"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
"""

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []

        for i in range(len(nums) - 3):

            if i != 0 and nums[i] == nums[i - 1]:
                continue
        
            for j in range(i + 1, len(nums) - 2):

                if j - 1 != i and nums[j - 1] == nums[j]:
                    continue

                elif sum(nums[i + 1:i + 4]) > target - nums[i]:
                    break

                elif sum(nums[-3:]) < target - nums[i]:
                    break

                elif len(nums[i + 1:]) == 3:
                    if sum(nums[i + 1:]) == target - nums[i]:
                        result.append([nums[i], nums[j], nums[j + 1], nums[j + 2]])
                        continue
                    else:
                        break

                left = j + 1
                right = len(nums) - 1

                while left < right:

                    if nums[i] + nums[j] + nums[left] + nums[right] == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])

                        while left < right:
                            if nums[left] == nums[left + 1]:
                                left += 1
                            else:
                                break

                        while left < right:
                            if nums[right] == nums[right - 1]:
                                right -= 1
                            else:
                                break

                        left += 1
                        right -= 1

                    elif nums[i] + nums[j] + nums[left] + nums[right] > target:
                        right -= 1

                    else:
                        left += 1

        return result             
