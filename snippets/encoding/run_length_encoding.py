"""
    ランレングス圧縮
"""

def run_length_encoding(s: str):
    """
        文字列をランレングスエンコーディングする

        Args:
            s: 変換したい文字列
        
        Returns:
            list[string, int]: [文字, 繰り返し数]のtupleのリスト
    """
    from itertools import groupby

    grp = groupby(s)
    res = []

    for k, v in grp:
        res.append((k, len(list(v))))
    return res

def run_length_decode(l: list):
    """
        ランレングス圧縮した[文字, 繰り返し数]のtupleのリストを文字列に変換する

        Args:
            l: エンコーディングした結果
        
        Returns:
            striing: デコードした文字列
    """
    raw = []
    for c, n in l:
        raw.append(c*n)
    
    res = ''.join(raw)

    return res
