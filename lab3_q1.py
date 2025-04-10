import math
numbers = list(map(int, input("Enter N numbers separated by space: ").split()))
mean = sum(numbers) / len(numbers)
variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
std_deviation = math.sqrt(variance)
print(f"Mean: {mean}")
print(f"Variance: {variance}")
print(f"Standard Deviation: {std_deviation}")
