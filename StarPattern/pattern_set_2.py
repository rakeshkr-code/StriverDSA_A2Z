# ## Pattern - 1:
#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *

n = int(input("Enter the number of rows: "))

print("## Pattern - 1:")
for i in range(n):
    for j in range(n-i-1):
        print(" ", end=" ")
    for j in range(2*i+1):
        print("*", end=" ")
    print()

# --------------------------------------------------------------

# ## Pattern - 2:
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *

print("## Pattern - 2:")
for i in range(n):
    for j in range(i):
        print(" ", end=" ")
    for j in range(2*(n-i)-1):
        print("*", end=" ")
    print()

# --------------------------------------------------------------

# ## Pattern - 3:
#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *

print("## Pattern - 3:")
for i in range(n):
    for j in range(n-i-1):
        print(" ", end=" ")
    for j in range(2*i+1):
        print("*", end=" ")
    print()
for i in range(n-1):
    for j in range(i+1):
        print(" ", end=" ")
    for j in range(2*(n-i-1)-1):
        print("*", end=" ")
    print()

# --------------------------------------------------------------

# ## Pattern - 4:
# *
# * *
# * * * 
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

print("## Pattern - 4:")
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print()
for i in range(n-1):
    for j in range(n-i-1):
        print("*", end=" ")
    print()

# --------------------------------------------------------------

# ## Pattern - 5:
# 1
# 0 1
# 1 0 1
# 0 1 0 1
# 1 0 1 0 1

print("## Pattern - 5:")
for i in range(n):
    for j in range(i+1):
        if (i+j) % 2 == 0:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()

# --------------------------------------------------------------

# ## Pattern - 6:
# 1            1
# 1 2        2 1
# 1 2 3    3 2 1
# 1 2 3 4 4 3 2 1

print("## Pattern - 6:")
for i in range(n):
    for j in range(i+1):
        print(j+1, end=" ")
    for j in range(2*(n-i-1), -1, -1):
        print(" ", end=" ")
    for j in range(i, -1, -1):
        print(j+1, end=" ")
    print()
