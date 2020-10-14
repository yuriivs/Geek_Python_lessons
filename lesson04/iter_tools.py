
# def some_number(start = 0):
#     yield start + 1

from itertools import count

for x in count(100, 2.5):
    if x > 200:
        break

    print(x)

print("Done")


