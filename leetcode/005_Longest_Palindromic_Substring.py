class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        for i, v in enumerate(s):
            res = max(self.helper(s, i, i), self.helper(s, i, i+1), res, key=len)
        return res
        
    def helper(self, raw_str, index_left, index_right):
        while index_left >= 0 and index_right < len(raw_str) and raw_str[index_left] == raw_str[index_right]:
            index_left -= 1
            index_right += 1
        
        return raw_str[index_left + 1:index_right]