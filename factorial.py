# Find the factorial of a number using a loop.

num = int(input("enter any no.: "))

fact = 1

for i in range(1, num+1):
    fact *= i

    print(f"the factorial of the {num} is: {fact}")