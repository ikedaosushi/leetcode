from bisect import bisect


def lis(seq):  # 最長増加部分列
    end = []  # すべての長さに対する最後尾の値
    for val in seq:  # すべての値を順に試す
        idx = bisect(end, val)  # 最後尾上に構築できるか
        if idx == len(end):
            end.append(val)  # 最長部分列を拡張
        else:
            end[idx] = val  # 前の最後尾の値を減らす
        print("end:", end)
    return len(end)  # 最長部分列を発見


print(lis([3, 1, 0, 2, 4, 1, 2, 5]))
