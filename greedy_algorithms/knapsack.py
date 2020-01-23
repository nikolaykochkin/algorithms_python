from typing import List


def knapsack(max_weight: int, items: List[List[int]]) -> float:
    items.sort(key=lambda i: i[0] / i[1], reverse=True)
    result: float = 0
    for cost, weight in items:
        if weight < max_weight:
            result += cost
            max_weight -= weight
        else:
            result += cost / weight * max_weight
            break
    return round(result, 3)


def main() -> None:
    n, knapsack_weight = map(int, input().split())
    items = [list(map(int, input().split())) for i in range(n)]
    print('{:.3f}'.format(knapsack(knapsack_weight, items)))


if __name__ == "__main__":
    main()
