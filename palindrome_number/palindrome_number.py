class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        t = x
        rev = 0
        if(x < 0):
            return False
        else:
            while(x > 0):
                rem = x % 10
                x //= 10
                rev = rev * 10 + rem
            return rev == t
        
if __name__ == '__main__':
    solution = Solution()
    input1 = 121
    input2 = -121
    input3 = 10
    print(f"Input: {input1}, Is Palindrome: {solution.isPalindrome(input1)}")
    print(f"Input: {input2}, Is Palindrome: {solution.isPalindrome(input2)}")
    print(f"Input: {input3}, Is Palindrome: {solution.isPalindrome(input3)}")
