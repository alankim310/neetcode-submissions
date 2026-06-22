class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for char in s:
            if len(s) == 0: 
                return False

            t_index = t.find(char)
            if t_index != -1:
                t = t[:t_index] + t[t_index + 1 :]
            else:
                return False
        
        if len(t) != 0 : return False
        return True