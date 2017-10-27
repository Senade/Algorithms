def search(n):
    b = 0
    for i in range((1<<n)):
        subset = []
        for j in range(0, n):
            if (i & (1 << j)):
                subset.append(j)
        print(subset)
        b += 1


def main():
    search(3)


if __name__ == '__main__':
    main()
