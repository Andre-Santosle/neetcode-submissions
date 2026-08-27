class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        else:
            map_s = {}
            map_t = {}

            for l in s:
                map_s[l] = map_s.get(l, 0) + 1

            for l in t:
                map_t[l] = map_t.get(l, 0) + 1

            for e in map_s:
                if map_s[e] != map_t.get(e, 0):
                    return False
                
            
            return True