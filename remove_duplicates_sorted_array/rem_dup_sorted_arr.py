class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) - 1
        i = 0
        j = 1
        while (i < n or j < n):
            if(nums[i] == nums[j]):
                nums.pop(j)
                n-=1
            else:
                i+=1
                j+=1
        return len(nums)
    
if __name__ == '__main__':
    solution = Solution()
    nums = [0,0,1,1,1,2,2,3,3,4]
    res = solution.removeDuplicates(nums)
    print(f"No of non duplicate elements: {res}, Unique Elements: {nums}")