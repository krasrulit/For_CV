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

from collections import defaultdict

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        positive = defaultdict(int)
        negative = defaultdict(int)
        zeros = 0

        for num in nums:
            if num > 0:
                positive[num] += 1
            elif num < 0:
                negative[num] += 1
            else:
                zeros += 1

        result = []

        if zeros > 0:
            for num in negative:
                if -num in positive:
                    result.append((0, num, -num))
            if zeros > 2:
                result.append((0, 0, 0))

        for set1, set2 in ((negative, positive), (positive, negative)):
            Set1List = list(set1.items())
            for i, (j, k) in enumerate(Set1List):
                for j2, k2 in Set1List[i:]:
                    if (j != j2) or (j == j2 and k > 1):
                        if -j-j2 in set2:
                            result.append((j, j2, -j-j2))

        return result
