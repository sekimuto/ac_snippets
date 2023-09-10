class KMP:
    """
        KMP法
    """

    def __init__(self, pattern: str):
        """
        Args:
            pattern: 対象文字列に含まれているか確認したいパターン
        """
        self.pattern = pattern
        self.l_p = len(self.pattern)
        self.table = [0 for _ in range(self.l_p)]

        j = 0
        for i in range(1, self.l_p):
            if self.pattern[i] == self.pattern[j]:
                j += 1
                self.table[i] = j
            else:
                self.table[i] = j
                j = 0
    
    def exec(self, s: str):
        """
            文字列検索を実行する

            Args:
                s: パターンが含まれているかを確認したい文字列
        """
        i = 0
        j = 0
        l_s = len(s)
        
        while i < l_s and j < self.l_p:
            if s[i] == self.pattern[j]:
                i += 1
                j += 1
            elif j == 0:
                i += 1
            else:
                j = self.table[j]
        
        if j == self.l_p:
            return i - j
        
        return None
