# Big O (n)
def print_n(n):
    for i in range(n): 
        print(i)
# This two loop is also consider as O(n) with constant drop
    for j in range(n):
        print(j)

# Big O (n sq)
def print_x(x):
    for i in range(x):
        for j in range(x): 
            print(i,j)

# Big O(1)
def add_item(n):
    return n + n


# # print_n(10)
# print_x(10)
# add_item(10)

