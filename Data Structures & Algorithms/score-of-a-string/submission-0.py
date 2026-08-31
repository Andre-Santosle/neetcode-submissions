class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0

        i = 0
        while i < len(s)-1:
            score += abs(ord((s[i+1]))-ord(s[i]))
            i += 1

        return score
