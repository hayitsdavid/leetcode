class Solution:
    """
    Time: O(text1 * text2)
    Space: O(text1 * text2)
    """

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        mp = {}

        def dp(c1, c2):
            if c1 < 0 or c2 < 0:
                return 0
            if (c1, c2) in mp:
                return mp[(c1, c2)]

            opt1 = dp(c1 - 1, c2)
            opt2 = dp(c1, c2 - 1)
            lrg = max(opt1, opt2)

            if text1[c1] == text2[c2]:
                opt3 = dp(c1 - 1, c2 - 1) + 1
                mp[(c1, c2)] = max(opt3, lrg)
                return mp[(c1, c2)]

            mp[(c1, c2)] = lrg
            return lrg

        return dp(len(text1) - 1, len(text2) - 1)
