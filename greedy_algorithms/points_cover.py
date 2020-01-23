from typing import List


def points_cover(segments: List[List[int]]) -> List[int]:
    sorted_segments: List[List[int]] = sorted(segments, key=lambda x: x[1])
    last: int = -1
    result: List = []
    for left, right in sorted_segments:
        if last < left:
            last = right
            result.append(right)
    return result


def main() -> None:
    n: int = int(input())
    segments: List[List[int]] = [list(map(int, input().split())) for i in range(n)]
    result: List[int] = points_cover(segments)
    print(len(result))
    print(*result)


if __name__ == '__main__':
    main()
