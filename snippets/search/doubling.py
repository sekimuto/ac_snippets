class Doubling:
    def __init__(self, n, k, a: list):
        k = max((k-1).bit_length(), 1)
        self.next = [[] * n for _ in range(k)]
        self.next[0] = a

        # あとは問題ごとのルールに従って、next[i-1]からnext[i]を求める

    def search(self, start, k):
        i = 0
        ans = start
        while k:
            if k & 1:
                ans = self.next[i][ans]
                k >> 1
                i += 1
        
        return ans
    