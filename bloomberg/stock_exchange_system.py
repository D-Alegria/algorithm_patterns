"""
    You are given a list of stock exchange along with startTime and endTime in which these exchanges operate.
    0 <= startTime, endTime <= 23

    [
        ['Exchange A', 2, 7],
        ['Exchange C', 11, 17],
        ['Exchange B', 9, 16],
        ['Exchange D',14, 20]
    ]
    Then, given a list of buy/sell orders which need to be executed in the given timeframe you need to find out what all
    orders can be served with atleast 1 exchange.

    [
        ['Order 1', '3', '6'],
        ['Order 2', '9', '12'],
        ['Order 3', '21', '22']
    ]
    So in this case Order 1 and 2 can be served but 3 cannot be served by any exchange.

    Follow-up= What if some exchanges operate from night to morning, ex - ['Exchange X', 23, 5]. Same thing with orders.
"""


class StockExchangeSystem:

    def __init__(self):
        self.operation = [[2, 7], [11, 17], [9, 16], [14, 20]]
        self.operation.sort(key=lambda x: x[0])

        result = [self.operation[0]]

        for i in range(1, len(self.operation)):
            current = result[-1]
            if current[1] >= self.operation[i][0]:
                result[-1][1] = max(current[1], self.operation[i][1])
            else:
                result.append(self.operation[i])

    def evaluate_orders(self, orders):
        result = []
        for name, start, end in orders:
            for start_o, end_o in self.operation:
                if int(start) >= start_o and int(end) <= end_o:
                    result.append([name, start, end])

        return result


if __name__ == '__main__':
    system = StockExchangeSystem()
    print(system.evaluate_orders([
        ['Order 1', '3', '6'],
        ['Order 2', '9', '12'],
        ['Order 3', '21', '22']
    ]))
