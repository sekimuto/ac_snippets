def calc_divisors(n: int, sort: bool=False):
    """目的や機能

        約数列挙を行う

        Args:
            n: 約数列挙を行いたい正の整数
            sort: 列挙した約数を昇順に並び替えるかどうか
        
        Returns:
            list[int]: 列挙された約数のリスト
    """

    res = []

    for i in range(1, n+1):
        # sqrt(n)を超えたらbreak
        if i ** 2 > n:
            break

        if n % i == 0:
            res.append(i)
            if n // i != i:
                res.append(n // 1)
    
    if sort:
        res.sort()
    return res
