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

# --------------------------------------------------------------

# ## Pattern - 4:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

print("## Pattern - 4:")
for i in range(n):
    for j in range(i+1):
        print(j+1, end=" ")
    print()

# --------------------------------------------------------------

# ## Pattern - 5:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

print("## Pattern - 5:")
for i in range(n):
    for j in range(i+1):
        print(i+1, end=" ")
    print()

# --------------------------------------------------------------

# ## Pattern - 6:
# * * * * *
# * * * * 
# * * * 
# * *
# *

print("## Pattern - 6:")
for i in range(n):
    for j in range(n-i):
        print("*", end=" ")
    print()

# --------------------------------------------------------------

# ## Pattern - 7:
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

print("## Pattern - 7:")
for i in range(n):
    for j in range(n-i):
        print(j+1, end=" ")
    print()

