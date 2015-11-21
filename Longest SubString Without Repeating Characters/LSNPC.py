class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        map = {}
        left = -1
        maxLenght = 0
        for right, c in enumerate(s):
            if c in map and map[c] > left:
                left = map[c]
            map[c] = right
            maxLenght = max(maxLenght, right - left)
        return maxLenght

str = "abcabcbb"
solution = Solution()
maxLenght = solution.lengthOfLongestSubstring(str)
print maxLenght