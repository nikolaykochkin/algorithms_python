from functools import lru_cache
import math
from typing import List, Tuple, Callable


def fib_math(n: int) -> int:
    SQRT5: float = math.sqrt(5)
    PHI: float = (SQRT5 + 1) / 2
    return int(PHI ** n / SQRT5 + 0.5)


@lru_cache(maxsize=None, typed=True)
def fib_recursive(n: int) -> int:
    assert n >= 0
    return fib_recursive(n - 1) + fib_recursive(n - 2) if n > 1 else n


def fib_dynamic(n: int) -> int:
    assert n >= 0
    a: int = 0
    b: int = 1
    for _ in range(1, n):
        a, b = b, a + b
    return a


Matrix = List[List[int]]


def pow(x: Matrix, n: int, I: Matrix, mult: Callable[..., Matrix]) -> Matrix:
    """
    Возвращает x в степени n. Предполагает, что I – это единичная матрица, которая 
    перемножается с mult, а n – положительное целое
    """
    if n == 0:
        return I
    elif n == 1:
        return x
    else:
        y: Matrix
        y = pow(x, n // 2, I, mult)
        y = mult(y, y)
        if n % 2:
            y = mult(x, y)
        return y


def identity_matrix(n: int) -> Matrix:
    """Возвращает единичную матрицу n на n"""
    r: List[int] = list(range(n))
    return [[1 if i == j else 0 for i in r] for j in r]


def matrix_multiply(A: Matrix, B: Matrix) -> Matrix:
    BT: List[Tuple[int]] = list(zip(*B))
    return [[sum(a * b
                 for a, b in zip(row_a, col_b))
             for col_b in BT]
            for row_a in A]


def fib_matrix(n: int) -> int:
    assert n >= 0
    F: Matrix = pow([[1, 1], [1, 0]], n,
                    identity_matrix(2), matrix_multiply)
    return F[0][1]


def main() -> None:
    n: int = int(input())
    print(fib_matrix(n))


if __name__ == "__main__":
    main()
