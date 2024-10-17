def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_all(1, 2, 3))        # Output: 6
print(sum_all(4, 5, 6, 7, 8))  # Output: 30
