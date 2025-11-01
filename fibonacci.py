# Write a program to print the Fibonacci series up to n terms.

n = int(input("enter any no.: "))

a, b = 0, 1

print("fibonacci series: ")

for i in range(n):
    print(a)
    a,b = b, a + b