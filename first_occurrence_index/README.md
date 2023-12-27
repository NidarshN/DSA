# Find the Index of the First Occurrence in the String

> **Topics:** *Two Pointers, String, String Matching*

[LeetCode #28](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

## Examples

``` text
Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
```

``` text
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
```

## Constraints

``` text
1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
```

[Python Solution](./first_occurence_index.py)
