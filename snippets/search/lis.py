"""
    LIS(最長増加部分列)を求めるアルゴリズム

    不連続な部分列でもできる一般的なもの
"""

def lis(a: list):
    from bisect import bisect_left
    n = len(a)

    lis = [a[0]]

    for i in range(n):
        # 最後尾より大きかったら末尾に追加
        if a[i] > lis[-1]:
            lis.append(a[i])
        
        # より小さい数字に更新できる場所があるので、その場所を二分探索で探す
        else:
            lis[bisect_left(lis, a[i])] = a[i]
    
    return len(lis)
