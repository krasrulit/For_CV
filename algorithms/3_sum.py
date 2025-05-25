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
