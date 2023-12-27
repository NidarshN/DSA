class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x < 0 else 1
        x *= sign
        rev = 0
        while(x > 0):
            rem = x % 10
            rev = (rev * (10)) + rem
            x //= 10
        rev *= sign
        if(rev < -(2**31) or rev > (2**31) - 1):
            return 0
        else:
            return rev

if __name__ == '__main__':
    solution = Solution()
    x = 123
    print(f"Result: {solution.reverse(x)}")

    x = -123
    print(f"Result: {solution.reverse(x)}")

    x = 120
    print(f"Result: {solution.reverse(x)}")

    x = 1563847412
    print(f"Result: {solution.reverse(x)}")
