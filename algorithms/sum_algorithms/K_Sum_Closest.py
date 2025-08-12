# можно улучшить использование памяти, заменив в рекурсии создание новых списков (self.KSumClosest(nums[i + 1:], target - nums[i], k - 1))
# на использование стартового индекса KSumClosest(self, nums, start, target, k) (start = i + 1)

class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        k = 3
        return self.KSumClosest(nums, target, k)

    def KSumClosest(self, nums, target, k):

        result = None
        
        if len(nums) == k:
            return sum(nums)
            
        elif sum(nums[:k]) >= target:
            return sum(nums[:k])
            
        elif sum(nums[-k:]) <= target:
            return sum(nums[-k:])

        elif k == 2:
            
            i = 0
            j = len(nums) - 1
            result = None
            
            while i < j:
                candidate = nums[i] + nums[j]
                
                if candidate == target:
                    return nums[i] + nums[j]
                    
                elif (result == None) or abs(target - candidate) < abs(target - result):
                    result = candidate
            
                elif candidate < target:
                    i += 1
            
                else:
                    j -= 1
        
            return result

        else:
            for i in range(len(nums) - k + 1):
                candidate = self.KSumClosest(nums[i + 1:], target - nums[i], k - 1) + nums[i]

                if candidate == target:
                    return candidate
                    
                elif result == None or abs(target - candidate) < abs(target - result):
                    result = candidate

        return result
