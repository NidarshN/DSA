class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        turns = nums.count(val)
        for _ in range(turns):
            nums.remove(val)
        return len(nums)
    

if __name__ == "__main__":
    solution = Solution()
    nums = [3,2,2,3]
    val = 3
    result = solution.removeElement(nums, val)
    print(f"Length of the result: {result}, Result: {nums}")

    nums = [0,1,2,2,3,0,4,2]
    val = 2
    result = solution.removeElement(nums, val)
    print(f"Length of the result: {result}, Result: {nums}")
