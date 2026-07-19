class StockSpanner:

    def __init__(self):
        self.stock_price = []
        self.stock_spanner = []
        

    def next(self, price: int) -> int:
        span = 1
        while self.stock_price and self.stock_price[-1] <= price:
            span += self.stock_spanner[-1]
            self.stock_price.pop()
            self.stock_spanner.pop()
        self.stock_price.append(price)
        self.stock_spanner.append(span)
        return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)