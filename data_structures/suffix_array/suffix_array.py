class SuffixArray:
    def __init__(self, s: str):
        self._string = s
        self.construct_naive(s)

    def construct_naive(self, s: str):
        """
        This naive construction takes O(n*n*logn) time
        """
        self.suffixarr = [i for i in range(len(s))]
        self.suffixarr.sort(key=lambda i: s[i:])

    def construct_better(self, s: str):
        """
        This algorithm constructs suffix array in O(n*logn*logn) time
        """
        pass

    def display(self):
        for i in range(len(self.suffixarr)):
            p = self.suffixarr[i]
            print(p, self._string[p:])
