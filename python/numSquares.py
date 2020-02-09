class Solution:
    def numSquares(self, n: int) -> int:
        if n in [0, 1]:
            return n

        cand = [i * i for i in range(1, int(n**(1 / 2)) + 1)]
        cnt = 0
        check = [n]
        while check:
            cnt += 1
            tmp = []
            for x in check:
                for y in cand:
                    if x == y:
                        return cnt
                    if x < y:
                        break
                    tmp.append(x - y)
            check = tmp

        return cnt


if __name__ == "__main__":
    n = 12
    actual = Solution().numSquares(n)
    print(actual)
