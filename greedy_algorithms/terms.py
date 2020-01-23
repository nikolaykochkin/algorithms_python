def terms(n):
    result = []
    cnt = 1
    while n > 2 * cnt:
        result.append(cnt)
        n -= cnt
        cnt += 1
    result.append(n)
    return result


def main() -> None:
    t = terms(int(input()))
    print(len(t))
    print(*t)


if __name__ == "__main__":
    main()
