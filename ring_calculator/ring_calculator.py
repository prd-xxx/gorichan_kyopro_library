# https://github.com/prd-xxx/gorichan_kyopro_library/blob/main/ring_calculator/ring_calculator.py
class RingCalculator:
    def __init__(self, size, base_index=0):
        self.size = size
        self.base_index = base_index
    def _normalize(self, index):
        return (index - self.base_index + self.size) % self.size
    def dist_clockwise(self, from_index, to_index):
        fr = self._normalize(from_index)
        to = self._normalize(to_index)
        return (to - fr + self.size) % self.size
    def dist_anticlockwise(self, from_index, to_index):
        return (self.size - self.dist_clockwise(from_index, to_index)) % self.size
