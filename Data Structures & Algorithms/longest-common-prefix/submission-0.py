class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        com_prefix = ""

        smallest_word = min(strs, key=len)

        i = 0
        for _ in range(len(smallest_word)):
            for word in strs:
                if smallest_word[i] != word[i]:
                    return com_prefix
            com_prefix += smallest_word[i]
            i += 1

        return com_prefix