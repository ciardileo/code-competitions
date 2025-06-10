def main():
    N = int(input())
    array = [int(x) for x in input().split()]

    # bubble sort
    for i in range(N - 1):
        for j in range(N - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j+1], array[j]

    print(*array, sep=" ")

if __name__ == "__main__":
    main()
