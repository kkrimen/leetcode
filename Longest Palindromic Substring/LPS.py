class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s
        center, reach, start, length = 1, 1, 0, 0
        tmpStr = '$#'
        for ss in s:
            tmpStr += ss
            tmpStr += '#'
        tmpStr += '@'
        tmpMap = {}
        for i in range(0, len(tmpStr)):
            tmpMap[i] = 0
        for i in range(2, len(tmpStr) - 1):
            mirrori = center * 2 - i
            tmpMap[i] = min(tmpMap[mirrori], reach - i) if i < reach else 0
            while tmpStr[i - tmpMap[i] - 1] == tmpStr[i + tmpMap[i] + 1]:
                tmpMap[i] += 1
            if (i + tmpMap[i]) > reach: 
                reach = i + tmpMap[i]
                center = i
            if tmpMap[i] > length:
                start = (i - tmpMap[i]) / 2
                length = tmpMap[i]
        print start, length
        return s[start:start + length]

solution = Solution()

tmpStr = 'abcdefedcbabcdefgfedcbadfwsdfs'

print solution.longestPalindrome(tmpStr)