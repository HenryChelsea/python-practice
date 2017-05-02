class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest_substr_dict = {}
        start = longest_str_len = 0
        if len(s) == 1:
            return 1
        for i,v in enumerate(s):
            if longest_substr_dict.get(v):
                longest_str_len = max(longest_str_len, len(longest_substr_dict))
                continue
            longest_substr_dict[v] = True

        longest_str_len = max(longest_str_len, len(longest_substr_dict))
        return longest_str_len

if __name__ == '__main__':
    test = 'pwwkew'
    solution = Solution()
    sub_str = solution.lengthOfLongestSubstring(test)
    print sub_str