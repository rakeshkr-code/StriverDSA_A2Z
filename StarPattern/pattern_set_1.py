# ## Pattern - 1:
# *****
# *****
# *****
# *****
# *****

# ## Code for Pattern - 1:
print("## Pattern - 1:")
n = int(input("Enter the number of rows: "))
for i in range(n):
    for j in range(n):
        print("*", end="")
    print()

# --------------------------------------------------------------

# ## Pattern - 2:
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

print("## Pattern - 2:")
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()

# --------------------------------------------------------------

# ## Pattern - 3:
# *
# * *
# * * *
# * * * *
# * * * * *

print("## Pattern - 3:")
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print()
