"""
    しゃくとり法のテンプレート

    以下は「特定区間の和」を条件にして区間抽出を行ったもの

    流れとしては、
    1. 範囲の右側を動かして広げていく
    2. 広げていく中で条件を超えたタイミングで左側を動かして範囲を狭める
    3. 条件に合致したらansに保存
"""

# 探索する配列
a = []

# 条件の境界
k = 100

def shaku(a, k):
    from collections import deque

    ans = []
    dq = deque()

    # 一時保存
    s = 0
    j = -1

    for i, ai in enumerate(a):
        dq.append((i, ai))
        s += ai

        while dq and s > k:
            j, rm = dq.popleft()
            s -= rm

        if s == k:
            ans.append((j+1, i))

    return ans
