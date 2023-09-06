def mex(s: list):
    """
        配列ないの非不整数に含まれない、最も最小の数
        配列サイズをNとすると、O(logN)で求められる
        ソート済み配列限定

        Args:
            s: MEXを調べたいソート済みリスト
    """
    if not s or s[0] > 0:
        return 0
    
    low = 1
    high = len(s) + 1

    while high - low:
        mid = (low + high) // 2
        if mid - 1 == s[mid-1]:
            low = mid
        else:
            high = mid
    
    return low
