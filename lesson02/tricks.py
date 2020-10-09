# 1
nums = [
    [1, 2, 3],
    [4, 5, 6],
]
joined = sum(nums, [])
print(joined)


#2
unique = [1, 2, 3, 3, 5]
unique = list(set(unique))
print(unique)

#3
# a = 10
# b = 20
a, b = 10, 20

a, b = b, a
print(a, b)

#4
total = [1, 2, 3, 1, 5]
print(
    max(
        set(total), key=total.count)
    )

#5
print(*total, end="", sep="=")