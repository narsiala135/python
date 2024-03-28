from collections import Counter
import statistics

def calculate_mean(arr):
    return sum(arr) / len(arr)

def calculate_median(arr):
    arr.sort()
    n = len(arr)
    if n % 2 == 0:
        return (arr[n//2 - 1] + arr[n//2]) / 2
    else:
        return arr[n//2]

def calculate_mode(arr):
    counter = Counter(arr)
    mode = counter.most_common(1)[0][0]
    return mode

def main():
    numbers = [
        16, 18, 27, 16, 23, 21, 19]  # Example array of numbers
    mean = calculate_mean(numbers)
    median = calculate_median(numbers)
    mode = calculate_mode(numbers)

    print("Mean:", mean)
    print("Median:", median)
    print("Mode:", mode)

if __name__ == "__main__":
    main()
