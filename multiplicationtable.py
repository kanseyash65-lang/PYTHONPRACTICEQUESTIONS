# Print the multiplication table of a number using a for loop.

num = int(input("Enter any no.: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")