def search(i, n, subset):
    if i == n:
        print(subset)
    else:
        # don't consider myself
        search(i + 1, n, subset)
        subset.append(i)
        # consider myself
        search(i + 1, n, subset)
        subset.pop()


def main():
    search(0, 3, [])


if __name__ == '__main__':
    main()
