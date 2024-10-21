# https://github.com/prd-xxx/gorichan_kyopro_library/blob/main/ring_calculator/ring_calculator.py
class RingCalculator:
    def __init__(self, size, base_index=0):
        self.size = size
        self.base_index = base_index
    def _normalize(self, index):
        return (index - self.base_index) % self.size
    def dist_clockwise(self, from_index, to_index):
        fr = self._normalize(from_index)
        to = self._normalize(to_index)
        return (to - fr) % self.size
    def dist_anticlockwise(self, from_index, to_index):
        return (self.size - self.dist_clockwise(from_index, to_index)) % self.size

rc = RingCalculator(5, base_index=1)
print(rc.dist_clockwise(3, 3)) # 0
print(rc.dist_clockwise(3, 4)) # 1
print(rc.dist_clockwise(3, 5)) # 2
print(rc.dist_clockwise(3, 1)) # 3
print(rc.dist_clockwise(3, 2)) # 4
print(rc.dist_anticlockwise(3, 3)) # 0
print(rc.dist_anticlockwise(3, 2)) # 1
print(rc.dist_anticlockwise(3, 1)) # 2
print(rc.dist_anticlockwise(3, 5)) # 3
print(rc.dist_anticlockwise(3, 4)) # 4
