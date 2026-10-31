numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

bin_size = int(input("Enter bin size: "))

hist = {}

for i in range(0, len(numbers), bin_size):
    start = numbers[i]
    end = start + bin_size - 1

    count = 0
    for num in numbers:
        if start <= num <= end:
            count += 1

    hist[f"{start}-{end}"] = count

print(hist)