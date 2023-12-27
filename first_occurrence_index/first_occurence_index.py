class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)
    
if __name__ == '__main__':
    solution = Solution()
    haystack = "sadbutsad"
    needle = "sad"
    print(f"Result: {solution.strStr(haystack, needle)}")

    haystack = "leetcode"
    needle = "leeto"
    print(f"Result: {solution.strStr(haystack, needle)}")