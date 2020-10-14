import sys
from lesson04 import my_mod

my_mod.calculate(10)

try:
    file, user, salary = sys.argv
except ValueError:
    print("Invalid args")
    exit()

my_mod.hello(user)
print(my_mod.calculate(int(salary)))
