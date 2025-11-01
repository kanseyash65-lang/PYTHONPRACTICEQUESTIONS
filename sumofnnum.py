# Find the sum of natural numbers up to n using a loop.

n = int(input("enter any no.: "))

total = 0

for i in range(1, n + 1):
    total += i

    print(f"the sum of natural no. upto {n} is {total}") 