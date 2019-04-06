class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        memo = [[0 for _ in range(n)] for _ in range(n)]
        max_len = 1
        i = 0
        while (i < n):
            memo[i][i] = True
            i = i + 1
            
        start = 0
        i = 0
        while i < n - 1:
            if(s[i] == s[i + 1]):
                memo[i][i + 1] = True
                start = i
                max_len = 2
            i = i + 1
        
        k = 3
        
        while k <= n:
            i = 0
            while i < (n - k +1):
                j = i + k - 1
                if (memo[i+1][j - 1] and s[i] == s[j]):
                    memo[i][j] = True
                    
                    if (k > max_len):
                        start = i
                        max_len = k
                        
                i += 1
            k += 1
            
        # printSubStr( str, start, start + maxLength - 1 ); 
        return s[start:start+max_len]
        