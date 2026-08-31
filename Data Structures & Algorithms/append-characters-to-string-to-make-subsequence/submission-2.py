class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        s_cursor = 0
        t_cursor = 0

        while s_cursor < len(s) and t_cursor < len(t):
            if s[s_cursor] == t[t_cursor]:
                t_cursor += 1
            s_cursor += 1

        return len(t) - t_cursor