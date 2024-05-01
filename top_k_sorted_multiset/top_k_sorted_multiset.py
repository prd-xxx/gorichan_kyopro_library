# ここにtatyam-primeさんのSortedMultiset.pyのコードを貼り付ける
# https://github.com/tatyam-prime/SortedSet/blob/main/SortedMultiset.py



# https://github.com/prd-xxx/gorichan_kyopro_library/tree/main/top_k_sorted_multiset.py
class TopKSortedMultiset:
    def __init__(self, k, arr:Iterable[T] = [], mode_max = True) -> None:
        assert k >= 0
        self.topk = SortedMultiset()
        self.other = SortedMultiset()
        self.k = k
        self.mode_max = mode_max
        self.sum_topk = self.sum_other = 0
        for a in arr:
            self.add(a)
    def _balance(self):
        while len(self.topk) > self.k:
            x = self.topk.pop(0 if self.mode_max else -1)
            self.sum_topk -= x
            self.other.add(x)
            self.sum_other += x
        while len(self.topk) < self.k and self.other:
            x = self.other.pop(-1 if self.mode_max else 0)
            self.sum_other -= x
            self.topk.add(x)
            self.sum_topk += x
    def add(self, x):
        self.topk.add(x)
        self.sum_topk += x
        self._balance()
    def discard(self, x):
        if x in self.topk:
            assert self.topk.discard(x)
            self.sum_topk -= x
        else:
            assert self.other.discard(x)
            self.sum_other -= x
        self._balance()
    def __len__(self):
        return len(self.topk) + len(self.other)
    def __str__(self):
        return str(self.topk) + " | " + str(self.other)
