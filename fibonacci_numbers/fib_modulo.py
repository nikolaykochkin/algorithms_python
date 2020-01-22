from typing import List


def fib_mod(n: int, m: int) -> int:
    fib: List[int] = [0, 1]
    pisano_period: int = 0
    for i in range(2, m * 6):
        fib.append((fib[i-1] + fib[i-2]) % m)
        pisano_period += 1
        if(fib[i] == 1 and fib[i-1] == 0):
            break
    return fib[n % pisano_period]


def main() -> None:
    n: int
    m: int
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()
