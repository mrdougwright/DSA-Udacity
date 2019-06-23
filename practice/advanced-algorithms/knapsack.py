import collections

Item = collections.namedtuple("Item", ["weight", "value"])


def max_value(knapsack_max_weight, items):
    """
    Get the maximum value of the knapsack.
    """
    weights = [0 for _ in range(knapsack_max_weight + 1)]

    for (weight, value) in items:
        for capacity in reversed(range(knapsack_max_weight + 1)):
            if weight <= capacity:
                weights[capacity] = max(
                    weights[capacity], weights[capacity - weight] + value
                )

    return weights.pop()


print(max_value(4, [Item(1, 7), Item(3, 8), Item(4, 9)]))
print(max_value(15, [Item(10, 7), Item(9, 8), Item(5, 6)]))
