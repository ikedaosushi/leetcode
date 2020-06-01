class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        w = []
        l = len(s)
        break_ = False
        for i in range(l):
            c = s[i]
            if c == " ":
                break_ = True
            else:
                if break_:
                    w = []
                    break_ = False
                w.append(c)
            
        return len(w)