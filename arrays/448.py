class Solution:
    def findDisappearedNumbers(self, nums):
        for n in nums:
            i = abs(n) - 1
            nums[i] = -1 * abs(nums[i])

        res = []
        for i, n in enumerate(nums):
            if n > 0:
                res.append(i+1)
        return res
    
    def grader(self, answer, output):
        if(output == answer):
            print(f'Success! \n {output}')
        else:
            print(f'Failure! \n {output}')
    
if __name__ == "__main__":
    solution = Solution()
    input1 = [4,3,2,7,8,2,3,1]
    output1 = solution.findDisappearedNumbers(input1)
    answer1 = [5,6]
    solution.grader(answer1, output1)
    input2 = [1,1]
    output2 = solution.findDisappearedNumbers(input2)
    answer2 = [2]
    solution.grader(answer2, output2)