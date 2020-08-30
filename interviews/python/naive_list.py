from itertools import combinations


def naive_list(seq):
    for length in range(len(seq), 0, -1):  # n, n-1, ... , 1
        for sub in combinations(seq, length):  # 与えられた列の部分列
            print(sub)
            if list(sub) == sorted(sub):  # 増加している列かどうかを確認
                return sub  # そうであれば、それを返す


print(naive_list([3, 1, 0, 2, 4]))
