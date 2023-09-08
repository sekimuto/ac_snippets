def lsb(num):
    """
        LSB(Least Significant Bit)を求めるビット演算。

        ある数を2進数表記したときに、右から数えて最初に1が現れる場所を求める。

        正確には、最初に1が現れるbitを右から`i`番目(`i ≥ 0`)とすると、`2^i`を返す。

        なので、「何番目」かがほしい場合は`bit_length`を使用する
    """
    return num & (-num)
