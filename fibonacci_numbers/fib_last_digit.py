def fib_digit(n: int) -> int:
    """This function calculates the last digit of the n-th Fibonacci number.
    Where n is integer number 1 <= n <= 10^7"""
    assert n > 0
    a: int = 0
    b: int = 1
    for _ in range(2, n + 1):
        a, b = b, (a + b) % 10
    return b


def main() -> None:
    n: int = int(input())
    print(fib_digit(n))


if __name__ == "__main__":
    main()
