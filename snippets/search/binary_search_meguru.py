"""
    めぐる式二分探索のテンプレート
    https://qiita.com/drken/items/97e37dd6143e33a64c8c

    solve関数に条件判定のロジックが入るイメージ
"""

def solve(a: list, mid, target) -> bool:
    if a[mid] > target:
        return True
    
    return False

def binary_search_meguru(a: list, target):
    n = len(a)
    right = n
    left = -1

    while right - left > 1:
        mid = (left + right) // 2
        if solve(a, mid, target):
            left = mid
        else:
            right = mid
    
    return left