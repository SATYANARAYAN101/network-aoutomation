def table(n, i=1):
    # Base case: stop after 10
    if i > 10:
        return
    # Print current line
    print(f"{n} x {i} = {n * i}")
    # Recursive call for next number
    table(n, i + 1)

# Take input from user
num = int(input("Enter number: "))
table(num)
