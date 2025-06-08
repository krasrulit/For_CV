"""
находит все уникальные суммы заданного количества чисел (k в функции fourSum), которые равны таргету 
finds all unique sums of a given number of numbers (k in the fourSum function) that are equal to the target
"""

class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        k = 4
        candidate = []
        result = []
        return self.K_Sum(nums, target, k, candidate, result)

    def K_Sum(self, nums, target, k, candidate, result):

        if sum(nums[:k]) > target:
            return result

        elif sum(nums[-k:]) < target:
            return result

        elif k == len(nums):
            if sum(nums) == target:
                result.append(candidate + nums)
            else:
                return result

        elif k == 2:

            left = 0
            right = len(nums) - 1

            while left < right:

                if nums[left] + nums[right] == target:
                    result.append(candidate + [nums[left], nums[right]])

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

                elif nums[left] + nums[right] > target:
                    right -= 1

                else:
                    left += 1

        else:
            for i in range(len(nums) - k + 1):

                if i > 0 and nums[i] == nums[i - 1]:
                    continue

                else:
                    candidate_new = candidate + [nums[i]]
                    self.K_Sum(nums[i + 1:], target - nums[i], k - 1, candidate_new, result)

        return result
