"""
## 標準入力受け取りの方法（stdin.readlineでの受け取り方）

### 前準備
from sys import stdin
readline = stdin.readline

### 整数の入力
n = int(readline())

### 文字列の入力（改行除去）
s = readline()[:-1]

### スペース区切りの整数の入力
a, b = map(int, readline().split())

### リストで受け取りたい場合
l = [*map(int, readline().split())]
"""

def main():
    from sys import stdin
    readline = stdin.readline

if __name__ == '__main__':
    main()
