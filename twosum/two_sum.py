class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        visited = {}
        for ind, val in enumerate(nums):
            compliment = target - nums[ind]

            if compliment in visited:
                return [visited[compliment], ind]
            
            visited[val] = ind

if __name__ == '__main__':
    solution = Solution()
    nums = [2,7,11,15]
    target = 9
    result = solution.twoSum(nums,target)
    print(result)
    
    nums = [3,2,4]
    target = 6
    result = solution.twoSum(nums,target)
    print(result)