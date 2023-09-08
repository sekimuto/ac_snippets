"""
    bit全探索のテンプレート
"""

n = 10

for bit in range(n ** 2):
    for i in range(n):
        if (bit >> i) & 1:
            # ここに処理を書く
            pass
