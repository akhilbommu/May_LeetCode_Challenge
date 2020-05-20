"""
https://leetcode.com/problems/online-stock-span/
"""


class OnlineStockSpan:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span = span + self.stack.pop()[-1]
        self.stack.append([price, span])
        return span


obj = OnlineStockSpan()
print(obj.next(100))
print(obj.next(80))
print(obj.next(60))
print(obj.next(70))
print(obj.next(60))
print(obj.next(75))
print(obj.next(85))
