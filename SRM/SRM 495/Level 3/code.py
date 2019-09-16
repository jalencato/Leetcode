def count(N, H):
    if H % N not in {0}:
        return -1
    return 1


if __name__ == '__main__':
    N = 2
    H = 58
    print(count(N, H))
