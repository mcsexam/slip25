def is_perfect(n):
    return sum(i for i in range(1, n) if n % i == 0) == n

numbers = [6, 28, 12, 496, 50, 8128, 100]

perfect_numbers = [n for n in numbers if is_perfect(n)]

print("Perfect numbers:", perfect_numbers)
