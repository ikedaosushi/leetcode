class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        for _ in range(n-1):
            let, tmp, count = s[0], "", 0
            for l in s:
                if let == l:
                    count += 1
                else:
                    tmp += str(count)+let
                    let = l
                    count = 1
            tmp += str(count) + let
            s = tmp
        
        return s