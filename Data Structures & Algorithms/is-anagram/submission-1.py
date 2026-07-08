class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False
        if sorted(s) == sorted(t):
            print(f's: {sorted(s)}, t:{sorted(t)}')
            return True
        else:
            return False